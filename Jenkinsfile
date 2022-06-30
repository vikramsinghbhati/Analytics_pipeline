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
          dir('/var/lib/jenkins/workspace/Jenkin-demo/'){

            pwd(); //Log current directory

            withAWS(region:'ap-south-1',credentials:'github-token') {

                 def identity=awsIdentity();//Log AWS credentials

                // Upload files from working directory 'dist' in your project workspace
               // s3Upload(bucket:"pysparkinp", workingDir:'/var/lib/jenkins/workspace/Jenkin-demo/', includePathPattern:'**/*');
               steps {
                sh 'aws s3 cp /var/lib/jenkins/workspace/Jenkin-demo/ s3://pysparkinp'
               }
            }

        };
      } catch(err) {
         sh "echo error in sending artifacts to s3"
      }
   }
}
