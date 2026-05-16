export async function onRequestPost(context) {
  const { request, env } = context;
  const formData = await request.formData();
  const token = formData.get('cf-turnstile-response');
  const ip = request.headers.get('CF-Connecting-IP');

  // Validate Turnstile
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
    return new Response('Invalid captcha', { status: 403 });
  }

  // Honeypot check
  if (formData.get('website')) {
    return new Response('Spam detected', { status: 400 });
  }

  // Data processing
  const name = formData.get('name');
  const email = formData.get('email');
  const message = formData.get('message');

  // NOTE: Here you would typically send an email using Mailchannels or a similar service
  // For now, we'll just log it or return a success message
  console.log(`New contact form submission from ${name} (${email}): ${message}`);

  // Redirect back or return JSON
  return new Response(null, {
    status: 302,
    headers: {
      'Location': '/kontakt.html?success=true'
    }
  });
}
