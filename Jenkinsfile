pipeline{
    agent any
    environment {
        SLACK_CHANNEL = "#it"
        SLACK_ICON_EMOJI = ":vinnieasa:"
        SLACK_USERNAME = "MemeBot"
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