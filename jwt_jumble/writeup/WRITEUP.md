# Writeup - jwt_jumble

As the name, this challenge is about **JWT** which is short for **JSON Web Token**.

These tokens are widely used to store some kind of session information like "logged in as admin".
The token is then given to the user by storing it in the users browser as a **cookie**.

To learn more about JWT, check out the [wikipedia article](https://en.wikipedia.org/wiki/JSON_Web_Token) or this [youtube video](https://www.youtube.com/watch?v=7Q17ubqLfaM).

After registering an account with dummy data, we see a flag button on the website which vanishes once we hover over it.
Checking the source code or using `Inspect Element` of our browser and clicking on the flag button, we learn that there is a endpoint `/flag` which we can access at.

On accessing `https://challenges.sshuzl.de/jwt_jumble/flag` we get the error message `You are not authorized to view the flag.`. Seems like the JWT token might contain
information about our authorization level?

To solve this challenge, we can use [this JWT editor](https://token.dev/) to modify our token. Then we edit our privileges to "admin" and set the
algorithm to `none`. We set it to `none` since we don't know the secret which the server uses to sign the token and hope that we can get along without a signature.

If we then change the cookie in our browser to the new JWT token which looks like this `encoded_header.encoded_payload`, we get the error from the website that our token
does not contain enough sections. The website seems to have expected a token like `encoded_header.encoded_payload.signature`. However the website is nice enough to tell us
that a trailing dot with an empty signature is fine. Updating our token to `encoded_header.encoded_payload.` (note the trailing dot), we access the endpoint `/flag` again and get the flag :)
