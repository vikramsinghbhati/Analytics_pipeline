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
          dir('/var/lib/jenkins/workspace/jenkin-demo'){

            pwd(); //Log current directory

            withAWS(region:'ap-south-1',credentials:'github-token') {

                 def identity=awsIdentity();//Log AWS credentials

                // Upload files from working directory 'dist' in your project workspace
               // s3Upload(bucket:"pysparkinp", workingDir:'/var/lib/jenkins/workspace/jenkin-demo/', includePathPattern:'**/*');
            
                sh 'aws s3 cp /var/lib/jenkins/workspace/jenkin-demo/ s3://pysparkinp/* --recursive --exclude "*" --include "*.py'
               
            }

        };
      } catch(err) {
         sh "echo error in sending artifacts to s3"
      }
   }
}
