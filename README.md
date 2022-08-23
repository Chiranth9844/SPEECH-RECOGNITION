# SPEECH-RECOGNITION
Python Mini Project


# Introduction

Speech is the most common means of communication around the world. Most of the population in the world relies on speech to communicate with each other. Suppose we are building a model and instead of a written approach we want our system to respond to speech, it becomes fairly difficult and requires a lot of data to be processed. A speech recognition system overcomes this barrier by translating speech to text.

# How Speech Recognition Works?

Speech recognition system basically translates the spoken utterances to text. There are various real-life examples of speech recognition system. For example- siri, which takes the speech as input and translates it into text.
The advantage of using a speech recognition system is that it overcomes the barrier of literacy. A speech recognition model can serve both literate and illiterate audience as well, since it focuses on spoken utterances.
We can also make an inventory of all the endangered languages around the world using a speech recognition system. While it looks pretty intriguing and not complex at all, a speech recognition system faces a lot of challenges in the making.


# Major modules with description

Installation of SpeechRecognition in Python

To install SpeechRecognition package is python, run the following command in the terminal and it will be installed on your system.

                          
![image](https://user-images.githubusercontent.com/53873995/186130354-3e17977c-ef29-4503-8ad9-79632ddd231d.png)


Audio Sources

The package has a Recognizer class which is basically where the magic happens. It is basically a class which is used to recognize the speech. Following are seven methods which can read various audio sources using different APIs.
•	recognize_bing( )
•	recognize_google( )
•	recognize_google_cloud( )
•	recognize_houndify( )
•	recognize_ibm( )
•	recognize_wit( )
•	recognize_sphinx( )

Now, recognize_sphinx can be used to run the speech recognition system offline as well. It requires the installation of Pocketsphinx.

         ![image](https://user-images.githubusercontent.com/53873995/186130308-df3445ea-dbd1-4ae8-b7c1-60ad7ad34aaf.png)


Taking Input from Microphones

To use the microphones, we will have to install pyaudio module as well. We use the microphone class to get the input speech from the microphone instead of any other input method like an audio file.
For most of the projects, we can use the default microphones. But if you do not wish to use the default microphone, you can get the list of microphone names using the list_microphone_names method.
To capture the input from the microphone we use the listen method.

          ![image](https://user-images.githubusercontent.com/53873995/186130392-ba0f589b-ce1f-44c8-8f74-05eaae4b652f.png)



Installation of PyAudio in Python

To install Pyaudio in python, run the following command in the terminal or if you are using pycharm add the package from the project interpreter in the settings.

           ![image](https://user-images.githubusercontent.com/53873995/186130451-e3d1ec82-b4d7-4806-96ba-5d451650c79b.png)
            


Use Case
We will make a program using the speechrecognition module in python to recognize speech and execute the following:
1.	convert the speech to text
2.	open a URL using web browser module
3.	pass a query using speech recognition to make a search in the URL
