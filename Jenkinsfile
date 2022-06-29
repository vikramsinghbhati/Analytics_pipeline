node('node'){
   stage('git checkout'){
      try {
      git credentialsId: 'github-token', url: 'https://github.com/vikramsinghbhati/Analytics_pipeline.git'
      } catch(err) {
         sh "echo error in checkout"
      }
   }
   
   stage('deployment of application') {
      try {
        sshagent(['ec2-user-target']){
           // clone the repo on target in tmp
            
            sh "scp -o StrictHostKeyChecking=no /Analytics_pipeline/*  ec2-user@65.0.204.176:/tmp"
            
            }
        } catch(err) {
           sh "echo error in deployment of an application"
        }
   
   stage('artifacts to s3') {
      try {
      // you need cloudbees aws credentials
      withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'github-token', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
         sh "aws s3 ls"
         sh "aws s3 cp /Analytics_pipeline/* s3://pysparkinp/"
         }
      } catch(err) {
         sh "echo error in sending artifacts to s3"
      }
   }
}
