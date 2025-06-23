## maubot-bible
A simple [maubot](https://github.com/maubot/maubot) module for Matrix servers that responds with a Bible verse (currently sourced from [bible-api.com](https://bible-api.com)).

## Usage
The trigger can be user-defined, but by default it is `!verse`.

To request a random verse, use `!verse random`.
To request a specific verse, use `!verse <book> <chapter>:<verse>` (case-insensitive)

Example: `!verse 1 corinthians 3:16`

## Installation
This plugin can be installed using the standard [maubot plugin instructions](https://docs.mau.fi/maubot/usage/basic.html#uploading-plugins).

## Functionality
This plugin defaults to King James Version translations due to 2 different APIs being consumed. Currently it is possible to request either a random verse, or a specific verse. `bible-api` provides several options to do specific look ups or return other translations, but they are not implemented at this time.

## Credits
Many thanks to `williamkray`, as this bot is based heavily on the code from their stock ticker plugin [maubot-ticker](https://github.com/williamkray/maubot-ticker).