# Writeup cirque_du_redirect

When accessing the website, we are being redirected to multiple pages. And as the challenge description suggest, one of the pages hides a secret.

We can analyze this behavior by using e.g. the network analyzer in the Chrome developer tools.

Using that, all the accessed sites will be listed. This is the case since our browser saves every network request we are performing.
With the network requests, we can also view the web servers response. Using that, we can also view so called "HTTP headers" which are sent
as part of the response from the web server. To learn more about HTTP header, check out this [wikipedia article](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields).

Looking at every http header from the visited sites, we can find a `X-Flag` header in one of the responses which contains the flag as its value.
