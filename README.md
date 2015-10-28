# sonarr-to-slackbot
Routes WebHooks from Sonarr to a Slack chat channel

1. Create a bot user in Slack
2. Copy the API key into the noted string in the Python file
3. Change the channel name in the Python file
3. On the Sonarr server, run "pip install slacker" ([more info on slacker here](https://github.com/os/slacker))
4. Run the Python script on the Sonarr server
5. In Sonarr go to Settings -> Connect, click the add button, click "Webhook"
6. Set URL to "http://localhost:8000", disable all switches except "On Download"
7. Name it, save it, done!
