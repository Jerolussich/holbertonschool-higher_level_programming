#!/usr/bin/node

const request = require('request');
const args = process.argv;

const options = {
    url: args[2],
    method: `GET`
}
const user_data = {}

request(options, function(err, resp, body) {
    let data = JSON.parse(body)

    data.forEach(task => {
        
        if (!user_data[task.userId])
        {
            user_data[task.userId] = 0;
        }
        if (task.completed == true)
        {
            user_data[task.userId]++;
        }
    });
    console.log(user_data)
})
