node('node'){
   stage('git checkout'){
      try {
      git credentialsId: 'github-token', url: 'https://github.com/vikramsinghbhati/Analytics_pipeline.git'
      } catch(err) {
         sh "echo error in checkout"
      }
   }
   
 
   
   stage('artifacts to s3') {
      try {
      // you need cloudbees aws credentials
      withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'github-token', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
         sh "aws s3 ls"
         
         }
      } catch(err) {
         sh "echo error in sending artifacts to s3"
      }
   }
}
