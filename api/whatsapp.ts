import { ServerRequest } from 'https://deno.land/std@0.58.0/http/server.ts';

export default async (req: ServerRequest) => {
  const u = new URL(req.url);
  const verification = u.searchParams.get('hub.challenge');
  req.respond({ body: `value="${verification}"` });
};
