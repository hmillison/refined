import { ServerRequest } from 'https://deno.land/std@0.58.0/http/server.ts';

export default async (req: ServerRequest) => {
  req.respond({ body: `value="1592314957"` });
};
