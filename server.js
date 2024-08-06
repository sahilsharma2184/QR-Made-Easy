import inquirer from "inquirer";
import qr from "qr-image";
import fs, { WriteStream } from "fs";

import nodemailer from 'nodemailer';
import express from 'express';

import pkg from 'pg';
const {Client}=pkg;
const client=new Client({
    host:'localhost',
    port:5432,
    database: 'QRMadeEasy', //database name in PSQL server
    user: 'postgres',
    password:'sahil@1810',
})
client.connect((err)=>{
    if(err){
        console.log('Error encountered while connecting to the database',err.stack)
        
    }else {
        console.log('Connected to the database')
        ask(); //once the database is connected then only the prompts will be taken 
        
    }
})
export default client;


function ask()
{
inquirer.prompt([
    {
        type: "input",
        message: "Type in your URL:",
        name: "URL",
    },
    {
        type: "input",
        message: "Enter Your Name:",
        name: "NAME",

        validate: function(value) {
            //relational function to check that if the entered name is valid or not
            var pass = value.match(/^[a-zA-Z]+(?:\s[a-zA-Z]+)+$/); 
            if (pass) {
                return true;
            }
            return "Enter a valid name";
        }
    },
    {
        type: "input",
        message: "Type in your email:",
        name: "EMAIL",

        validate: function(value) {
            //relational function to check that if the entered maid id is valid or not
            var pass = value.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/);
            if (pass) {
                return true;
            }
            return "Enter a valid email address";
        }
    },
])
.then((answers) => {
    const url = answers.URL;
    const email = answers.EMAIL;
    const name = answers.NAME;

    // Generating QR code
    var qr_svg = qr.image(url); 

    // QR image to png file
    const writeStream=qr_svg.pipe(fs.createWriteStream("qr_img.png")); 

    writeStream.on('error', (err) => { 
        //error handling incase any error occured during execution
        console.error(err);
    });

    writeStream.on('finish',()=>
        {
        //showing the message incase of successful execution of code and generation of the PNG file of the QR
        console.log("PNG file has been saved");
        })
    
    // URL to text file named URL.txt
    fs.writeFile("URL.txt", url, (err) => 
        {
        //throwing error incase any error encountered
        if (err) throw err;
        //showing the message incase of successful execution of code and generation of the .txt file of the QR
        console.log("URL file has been saved");
        process.exit(0);
    });

    //process.exit so that the console gets closed and exited after successful execution of the code

})
.catch((error) => {
    //error incase any error has been encountered durin the whole prompt activity
    console.error("An error occurred during prompt:", error);
});
}
/*
const html=`
<h1>Hello World</h1>
<p>Isn't nodemailer useful?</p>
`;
  
async function mail() {
    // Create a Nodemailer transporter
    const transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com', // Assuming you're using Gmail SMTP
        port: 587,
        secure: false, // true for 465, false for other ports
        auth: {
            user: 'rksahil1804@gmail.com',
            pass: 'ravi@1114' // Be sure to use an app-specific password if using Gmail
        }
    });
    const mailOptions = {
        from: 'rksahil1804@gmail.com',
        to: 'sharma_sahil@srmap.edu.in',
        subject: 'QR Code and URL',
        html: html,
        attachments: [
            {
                filename: 'qr_img.png',
                path: 'qr_img.png'
            },
            {
                filename: 'URL.txt',
                content: fs.createReadStream('URL.txt') // Attach the text file content
            }
        ]
    };
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log('Error occurred while sending email:', error.message);
        }
        console.log('Mail sent successfully!', info.messageId);
    });
}

// Call the mail function to send the email with attachments
mail();*/
// app.post('/generateQr', generateQr())

//actuak end pts here


// app.listen('3000')
