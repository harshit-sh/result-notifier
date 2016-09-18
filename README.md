# result-notifier

Get notified whenever college semester results are updated on [Campus Metalink](http://iiitb.campusmetalink.com/cml/pages/selfService/CssAssignmentReg.jsf).

## How does it work?

- Hosted on a [DigitalOcean](https://www.digitalocean.com) droplet.
- `Username` and `Term` fields are read from `config.yml` which is a `YAML` file. These fields should be changed accordingly, depending on the `roll-no`.
- The fields `password`, `twilio_no`, `your_no`, `Twilio auth tokens` (sensitive fields) are read as environment variables. Export them in the shell.
- Maximum number of courses is set to `5`. Can be changed accordingly.
- `Selenium` is used with `PhantomJS` to enter the fields and reach the page with the results table.
- Using [Twilio](https://www.twilio.com)'s `REST` API, messages are sent to the registered user as and when the results are updated.

## ToDo

- Catch errors for the event if the website goes down.
- Ensure correct parameters are passed and give appropriate response.

