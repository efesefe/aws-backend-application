1. Code gets committed to GitHub.
2. GitHub Actions workflow gets triggered.
3. The gh actions pipeline first assumes a role that was previously created on AWS. This logic removes the necessity to store AWS user credentials as a variable in GitHub.
4. It then uses serverless action to deploy the lambda instance using the yaml file and the code that exists inside the Lambda folder.
5. After deploying lambda, it continues with building a Docker image for testing and pushes this test image to Elastic Container Registry then in the next step uses that image to run tests. If tests are successful it builds normal image which is deployment ready and pushes it to the Elastic Container Registry. It tags every new image that is build with the last commit hash to the main branch. This allows us to store many versions of our application and anytime we want we may go back to an older version of our application.


![awsbackend](https://github.com/efesefe/aws-backend-application/assets/62351075/52f5ba16-fdfd-4b57-9132-d20a2b68ed16)
