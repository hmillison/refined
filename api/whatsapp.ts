import { Handler } from 'https://deno.land/std@0.150.0/http/server.ts';

export default <Handler>((req) => {
  const u = new URL(req.url);
  const verification = u.searchParams.get('hub.challenge');
  return new Response(`value="${verification}"`);
});
