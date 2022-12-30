pipeline {
    environment {
        WEBHOOK_URL = credentials("DISCORD_WEB_HOOK_URL")
    }
    triggers {
        pollSCM('* * * * *')
    }
    agent {
        label 'python3'
    }
    stages {
        stage("Run program") {
            steps {
                sh "python3 ./calculator.py 2 5"
            }
        }
        stage("Unit test") {
            steps {
                sh "python3 ./test_calculator.py"
            }
        }
    }
    post {
        success {
            discordSend description: "테스트 빌드가 성공했습니다",
            link: env.BUILD_URL, result: currentBuild.currentResult,
            webhookURL: env.WEBHOOK_URL
        }
        failure {
            discordSend description: "테스트 빌드가 실패했습니다",
            link: env.BUILD_URL, result: currentBuild.currentResult,
            webhookURL: env.WEBHOOK_URL
        }
    }
}