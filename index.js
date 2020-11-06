const Discord = require("discord.js");
const config = require("./config.json");
const client = new Discord.Client();

client.login(config.BOT_TOKEN);

const prefix = "&&";

client.on("message", function(message) {
	if (message.author.bot) return;
	if (!message.content.startsWith(prefix)) return;
	const commandBody = message.content.slice(prefix.length);
	const args = commandBody.split(' ');
	const command = args.shift().toLowerCase();
	if (command === "hi") {
		//const timeTaken = Date.now() - message.createdTimestamp;
		message.reply(`hello!`);
	}
	else if (command === "sum") {
    	const numArgs = args.map(x => parseFloat(x));
    	const sum = numArgs.reduce((counter, x) => counter += x);
    	message.reply(`The sum of all the arguments you provided is ${sum}!`);
	}
	else if (command === "multiplication") {
    	const numArgs = args.map(x => parseFloat(x));
    	const mul = numArgs.reduce((counter, x) => counter *= x);
    	message.reply(`The multiplication of all the arguments you provided is ${mul}!`);
	}
	else if (command == "name") {
		message.reply(`my name is NodeJs-Controlled-Le-Communism!`)
	}
	else if (command == "say") {
		message.channel.send(args)
	}
	else if (command == "spam") {
		message.reply(`only you can do such crazy things!`)
		for (var i = 0; i < args[0]; i += 1) {
			message.channel.send(args[1])
		}
	}
	else if (command == "clear") {
		const amount = parseInt(args[0]); // Количество сообщений, которые должны быть удалены
		if (!amount) {
			return message.reply('You have not written how many messages to delete!'); // Проверка, задан ли параметр количества
		}
		if (isNaN(amount)) {
			return message.reply('The thing you have written is not a number!'); // Проверка, является ли числом ввод пользователя 
		}
		if (amount > 100) {
			return message.reply('You can`t delete more the 100 messages!'); // Проверка, является ли ввод пользователя числом больше 100
		}
		if (amount < 1) {
			return message.reply('You have to write a number more than 0'); // Проверка, является ли ввод пользователя числом меньше 1
		}
		var u = message.channel;
		for (var i = 0; i < amount; i += 1) {
			
			u.lastMessage.delete()
		  		//.then(msg => message.channel.send(`Deleted message from ${msg.author.username}`))
				.catch(console.error);
			if (!u.lastMessage.deleted) {
				console.log("Be carful, maby an error occured!\n");
				u.lastMessage.delete();
			}
		}
	}
	else if (command == "setnamech") {
		message.channel.setName(args[0]);
	}
	else{
		//
		message.reply("Sorry, we can't find your command.", {
            files: [
                "./error.png"
            ]
        })
	}
});

client.login(config.BOT_TOKEN);
