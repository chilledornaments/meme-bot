pipeline{
    agent any
    environment {
        SLACK_CHANNEL = "#it"
        SLACK_ICON_EMOJI = ":vinnieasa:"
        SLACK_USERNAME = "MemeBot"
    }

    triggers {
        cron('H * * * 0-5')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages{
        stage("Meme goodness"){
            steps{
                withCredentials(
                    [
                        string(credentialsId: 'MEMEBOT_WEBHOOK', variable: 'SLACK_WEBHOOK')
                    ]
                ){
                    script{
                        sh '''
                        pip3 install --user -r reqs.txt
                        python3 bot/bot.py
                        '''
                    }
                }
                
            }
        }
    }
}