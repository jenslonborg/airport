### Personal Notes

This is used for personal notes regarding this project. 

#### Usefull command lines

When running any `fly` command on pc use `flyctl` instead. The fly.exe does not exist in the bin share `C:\Users\Jens Lønborg\.fly\bin`
`flyctl auth whoami` will tell you which email account is signed into fly

`flyctl ips list --app jens-lonborg-airport` list all available IP's. There will be a v4 and v6. Confirm that v4 is shared, else it will cost 2$ per month.

`flyctl config show --app jens-lonborg-airport` check the config of the app <br>
`fly apps list` will list all apps with their names

`flyctl scale count 0 --app jens-lonborg-airport --yes` turn off the app but don't delete it. This will only cost storage space which is 0.15 $ per GB. This will make the application inaccesable from a browser. So you cannot call `jens-lonborg-airpot.fly.dev anymore`. <br>
The application will still be visable from https://fly.io/dashboard/jens-lonborg. It will just be suspended
`flyctl scale count 1 --app jens-lonborg-airport --yes` will turn on the application again. Now you can call `jens-lonborg-airpot.fly.dev`

`flyctl scale show --app jens-lonborg-airport` shows the scale of the app. COUNT column indicates the scale set.

`flyctl apps destroy jens-lonborg-airport` will destroy the application completely. It will not even be visible here https://fly.io/dashboard/jens-lonborg

`flyctl apps list` list all applications and their status

#### Claude code ####

In Claude code you can check tokan usage via: `/usage`