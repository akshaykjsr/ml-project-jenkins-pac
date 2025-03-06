node {
    stage('Clone Repository') {
        git 'https://github.com/akshaykjsr/ml-project-jenkins-pac.git'
    }

    stage('Setup Environment') {
        sh '''
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        '''
    }

    stage('Train Model') {
        sh '''
        source venv/bin/activate
        python src/train.py
        '''
    }

    stage('Run Integration Tests') {
        sh '''
        source venv/bin/activate
        python src/test_model.py
        '''
    }

    stage('Deploy') {
        echo "Deployment stage (expand as needed)"
    }
}
