node {
    stage('Build') {
        withDockerContainer(image: 'python:2-alpine') {
            checkout scm
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            stash(name: 'compiled-results', includes: 'sources/*.py*')
        }
    }
    stage('Test') {
        withDockerContainer(image: 'qnib/pytest') {
            checkout scm
            sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            junit 'test-reports/results.xml'
            
        }
    }
    // stage('Manual Approval') {
    //     input message: 'Lanjutkan ke tahap Deploy?', ok: 'Yes, deploy'
    // }
    stage('Deploy') {
        checkout scm
        withEnv(["VOLUME=\$(pwd)/sources:/src", "IMAGE=cdrx/pyinstaller-linux:python2"]) {
            dir(env.BUILD_ID) {
                unstash(name: 'compiled-results')
                sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'"
                withDockerContainer(image: 'python:3-alpine', args: '-p 5000:5000') {
                    echo "Access the app at http://localhost:5000"
                    sh 'python sources/download.py -l & sleep 60'
                }
                archiveArtifacts "sources/dist/add2vals"
                sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
            }
        }
        // withCredentials([usernamePassword(credentialsId: 'heroku', usernameVariable: 'HEROKU_USER', passwordVariable: 'HEROKU_API_KEY')]) {
        //     withEnv(["APP_NAME=jenkins-pyinstaller", "IMAGE=registry.heroku.com/${APP_NAME}/web"]) {
        //         sh "docker login --username=_ --password=${HEROKU_API_KEY} registry.heroku.com"
        //         sh "docker build -t ${IMAGE} sources/dist/add2vals"
        //         sh "docker push ${IMAGE}"
        //         sh "heroku container:release web --app ${APP_NAME}"
        //     }
        // }
        
    }
}