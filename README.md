# Tokio-TheVoiceAssistant
> Ever wanted a J.A.R.V.I.S of your own? Well, you can start here. Tokio is a Personal Voice Assistant which takes in your command through microphone and performs the task as you wanted.

## Requirements
```sh
pip install -r requirements.txt
```
- Note: I had Chrome Brower version 85.x so I also install chromedriver 85.x. Download and replace the chromedriver according to your brower

## Usage example
```sh
python Tokio.py
```
- Tokio will start listening and you can give the following commands

| Command      | Function                                           |
|--------------|----------------------------------------------------|
| open website | to open almost any website                         |
| recommend    | recommend latest best movies according to IMDB     |
| play song    | to play any video in youtube                       |
| reviews      | to get movie reviews                               |
| infromation  | to get info about anything(fetched from wikipedia) |
| open         | to open installed software                         |
| create new   | to create and make note in a file                  |

- Note: Last 2 functions only work on Windows as of now.

## Development setup
- Follow the instructions in the requirements section above
- To add any kind of Automation(example open subreddit)
  - create a .py script in Automation package
  - import that script in assistance.py under Actions package.
  - add an elif condition
  - done
  
## Release History
* 0.0.1
    * Work in progress
    
## Meta
Manoj Kumar Tiwari 
– manojtiwari1.1v@gmail.com
– [@iManoj_Tiwari](https://twitter.com/iManoj_Tiwari)
– [Manoj Tiwari](https://www.linkedin.com/in/manoj-tiwari-3a3a6010a/)

Distributed under the MIT license. See ``LICENSE`` for more information.

## References
- https://realpython.com/python-speech-recognition/
- https://towardsdatascience.com/build-your-first-voice-assistant-85a5a49f6cc1
- https://www.slanglabs.in/blog/how-to-build-python-transcriber-using-mozilla-deepspeech
- https://www.youtube.com/watch?v=7Mwcmo1o_ik
- https://blog.rasa.com/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/
- https://www.youtube.com/watch?v=H9ZJ1uT8RFw&list=PLzMcBGfZo4-mBungzp4GO4fswxO8wTEFx&index=8
- https://techwithtim.net/tutorials/voice-assistant/opening-programs/


