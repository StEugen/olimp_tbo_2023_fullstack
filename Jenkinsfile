pipeline {
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/StEugen/olimp_tbo_2023_fullstack', branch: 'main', changelog: true)
      }
    }

  }
}