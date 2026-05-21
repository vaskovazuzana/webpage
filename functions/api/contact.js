export async function onRequestPost(context) {
  const { request, env } = context;
  const formData = await request.formData();
  const token = formData.get('cf-turnstile-response');
  const ip = request.headers.get('CF-Connecting-IP');

  let turnstileFormData = new FormData();
  turnstileFormData.append('secret', env.TURNSTILE_SECRET_KEY);
  turnstileFormData.append('response', token);
  turnstileFormData.append('remoteip', ip);

  const result = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    body: turnstileFormData,
    method: 'POST',
  });

  const outcome = await result.json();
  if (!outcome.success) {
    return new Response(
      'Invalid captcha: ' + JSON.stringify(outcome),
      { status: 403 }
    );
  }


  if (formData.get('website')) {
    return new Response('Spam detected', { status: 400 });
  }

  const name = formData.get('name');
  const email = formData.get('email');
  const message = formData.get('message');

  const resendResponse = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: 'Kontakt <web@mail.vaskova.space>',
      to: ['zuzana@vaskova.space'],
      reply_to: email,
      subject: `Nová správa z formulára od ${name}`,
      html: `
        <h2>Nová správa z kontaktného formulára</h2>
        <p><strong>Meno:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Správa:</strong></p>
        <p>${message}</p>
      `,
    }),
  });

  if (!resendResponse.ok) {
    return new Response('Email sending failed', { status: 500 });
  }

  return new Response(null, {
    status: 302,
    headers: {
      'Location': '/kontakt.html?success=true'
    }
  });
}
