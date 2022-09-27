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
    stage('Deliver') {
        withDockerContainer(image: 'cdrx/pyinstaller-linux:python2', args: '-v $(pwd)/sources:/src') {
            checkout scm
            unstash(name: 'compiled-results')
            sh 'pyinstaller -F add2vals.py'
            archiveArtifacts 'sources/dist/add2vals'
            sh 'rm -rf build dist'
        }
    }
}