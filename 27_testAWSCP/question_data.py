import uuid

# Define the question bank data
question_bank = [
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary benefit of using Amazon S3?',
        'choices': [
            'Storing and retrieving data over the internet',
            'Running virtual servers in the cloud',
            'Managing relational databases',
            'Building scalable web applications'
        ],
        'correct_answer': 'Storing and retrieving data over the internet'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to deploy and manage containers?',
        'choices': [
            'Amazon S3',
            'Amazon RDS',
            'Amazon ECS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is AWS Lambda used for?',
        'choices': [
            'Managing virtual networks',
            'Storing data in a scalable manner',
            'Running code in response to events',
            'Provisioning virtual machines'
        ],
        'correct_answer': 'Running code in response to events'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to distribute content globally with low latency?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'AWS Direct Connect',
            'Amazon VPC'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of Amazon EC2?',
        'choices': [
            'Storing large amounts of data',
            'Managing containerized applications',
            'Provisioning virtual servers in the cloud',
            'Deploying serverless applications'
        ],
        'correct_answer': 'Provisioning virtual servers in the cloud'
    },
        {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary storage class in Amazon S3 designed for frequently accessed data?',
        'choices': [
            'Amazon S3 Glacier',
            'Amazon S3 Intelligent-Tiering',
            'Amazon S3 Standard',
            'Amazon S3 Standard-IA'
        ],
        'correct_answer': 'Amazon S3 Standard'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed NoSQL database?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon DynamoDB'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service allows you to create private connections between AWS services and your datacenter?',
        'choices': [
            'Amazon VPC',
            'AWS Direct Connect',
            'Amazon Route 53',
            'Amazon CloudFront'
        ],
        'correct_answer': 'AWS Direct Connect'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service enables you to scale applications automatically in response to demand?',
        'choices': [
            'Amazon EC2',
            'Amazon RDS',
            'AWS Lambda',
            'Amazon Auto Scaling'
        ],
        'correct_answer': 'Amazon Auto Scaling'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service that allows you to monitor and manage your AWS resources and applications?',
        'choices': [
            'Amazon CloudWatch',
            'Amazon Inspector',
            'Amazon Route 53',
            'Amazon VPC Flow Logs'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to distribute incoming application traffic across multiple targets?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'AWS Elastic Load Balancing',
            'Amazon API Gateway'
        ],
        'correct_answer': 'AWS Elastic Load Balancing'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used to store and query unstructured data?',
        'choices': [
            'Amazon RDS',
            'Amazon Redshift',
            'Amazon DynamoDB',
            'Amazon S3'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to create and manage relational databases?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon S3'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of AWS IAM?',
        'choices': [
            'Managing user authentication and authorization',
            'Analyzing logs and metrics',
            'Optimizing network traffic',
            'Securing data at rest'
        ],
        'correct_answer': 'Managing user authentication and authorization'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to register and manage internet domain names?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'Amazon API Gateway',
            'AWS Direct Connect'
        ],
        'correct_answer': 'Amazon Route 53'
    },
        {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides scalable object storage in the cloud?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon S3',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used to securely manage access to AWS resources?',
        'choices': [
            'Amazon IAM',
            'Amazon EC2',
            'Amazon S3',
            'Amazon Lambda'
        ],
        'correct_answer': 'Amazon IAM'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service enables you to analyze and visualize log data in real-time?',
        'choices': [
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon CloudWatch',
            'AWS Lambda'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary benefit of using Amazon RDS?',
        'choices': [
            'Serverless computing',
            'Distributed file storage',
            'Managed relational databases',
            'Content delivery network'
        ],
        'correct_answer': 'Managed relational databases'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to run code without provisioning or managing servers?',
        'choices': [
            'Amazon S3',
            'Amazon EC2',
            'Amazon Lambda',
            'Amazon RDS'
        ],
        'correct_answer': 'Amazon Lambda'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service allows you to create and manage virtual networks in the cloud?',
        'choices': [
            'Amazon VPC',
            'Amazon Route 53',
            'Amazon CloudFront',
            'AWS Direct Connect'
        ],
        'correct_answer': 'Amazon VPC'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed data warehouse solution?',
        'choices': [
            'Amazon S3',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon Redshift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used to orchestrate multiple AWS resources into workflows?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'Amazon SQS',
            'Amazon Step Functions'
        ],
        'correct_answer': 'Amazon Step Functions'
    },
     {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for content delivery and acceleration of web content?',
        'choices': [
            'Amazon S3',
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon API Gateway'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides scalable and flexible block storage for EC2 instances?',
        'choices': [
            'Amazon EBS',
            'Amazon S3',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon EBS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary use case for Amazon DynamoDB?',
        'choices': [
            'Data warehousing',
            'Relational databases',
            'NoSQL databases',
            'Object storage'
        ],
        'correct_answer': 'NoSQL databases'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to securely encrypt and manage keys used for encryption?',
        'choices': [
            'Amazon KMS',
            'Amazon CloudHSM',
            'AWS Certificate Manager',
            'Amazon Macie'
        ],
        'correct_answer': 'Amazon KMS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service that allows you to create and manage virtual servers in the cloud?',
        'choices': [
            'Amazon RDS',
            'Amazon EC2',
            'Amazon S3',
            'Amazon VPC'
        ],
        'correct_answer': 'Amazon EC2'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to create and manage scalable relational databases?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon S3'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the primary purpose of Amazon SQS?',
        'choices': [
            'Streaming video content',
            'Managing queues of messages',
            'Storing large volumes of data',
            'Running serverless code'
        ],
        'correct_answer': 'Managing queues of messages'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used to register and manage domain names?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'Amazon API Gateway',
            'AWS Direct Connect'
        ],
        'correct_answer': 'Amazon Route 53'
    },
      {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of AWS Elastic Beanstalk?',
        'choices': [
            'Deploying and managing applications in the cloud',
            'Managing virtual networks',
            'Running code in response to events',
            'Creating and managing virtual machines'
        ],
        'correct_answer': 'Deploying and managing applications in the cloud'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to set up, operate, and scale a relational database in the cloud?',
        'choices': [
            'Amazon S3',
            'Amazon DynamoDB',
            'Amazon RDS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for real-time streaming of big data?',
        'choices': [
            'Amazon S3',
            'Amazon DynamoDB',
            'Amazon Kinesis',
            'Amazon CloudFront'
        ],
        'correct_answer': 'Amazon Kinesis'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to create and manage APIs?',
        'choices': [
            'Amazon API Gateway',
            'Amazon S3',
            'AWS Lambda',
            'Amazon EC2'
        ],
        'correct_answer': 'Amazon API Gateway'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of AWS CloudFormation?',
        'choices': [
            'Creating and managing virtual machines',
            'Orchestrating multiple AWS resources',
            'Storing and retrieving data over the internet',
            'Running code in response to events'
        ],
        'correct_answer': 'Orchestrating multiple AWS resources'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a scalable, highly available, and fully managed file storage solution?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon EFS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for adding security to your applications by controlling access?',
        'choices': [
            'Amazon IAM',
            'Amazon VPC',
            'Amazon Route 53',
            'Amazon CloudFront'
        ],
        'correct_answer': 'Amazon IAM'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to create and manage virtual machines in the cloud?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'AWS Lambda',
            'Amazon RDS'
        ],
        'correct_answer': 'Amazon EC2'
    },
     {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides scalable computing capacity in the cloud?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'Amazon RDS',
            'Amazon Lambda'
        ],
        'correct_answer': 'Amazon EC2'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for content delivery and acceleration through a global network of data centers?',
        'choices': [
            'Amazon S3',
            'Amazon EC2',
            'Amazon CloudFront',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of AWS Lambda?',
        'choices': [
            'Managing virtual networks',
            'Storing and retrieving data over the internet',
            'Running code in response to events',
            'Creating and managing virtual machines'
        ],
        'correct_answer': 'Running code in response to events'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for real-time messaging and communication between components of distributed applications?',
        'choices': [
            'Amazon SNS',
            'Amazon SQS',
            'Amazon SES',
            'Amazon SWF'
        ],
        'correct_answer': 'Amazon SNS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used to distribute incoming application traffic across multiple targets?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'AWS Elastic Load Balancing',
            'Amazon API Gateway'
        ],
        'correct_answer': 'AWS Elastic Load Balancing'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a managed message broker for cloud applications?',
        'choices': [
            'Amazon SNS',
            'Amazon SQS',
            'Amazon SES',
            'Amazon SWF'
        ],
        'correct_answer': 'Amazon SQS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed container orchestration service?',
        'choices': [
            'Amazon ECS',
            'Amazon EKS',
            'Amazon EC2',
            'AWS Lambda'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to create a virtual private cloud (VPC) for your AWS resources?',
        'choices': [
            'Amazon VPC',
            'Amazon EC2',
            'Amazon S3',
            'Amazon RDS'
        ],
        'correct_answer': 'Amazon VPC'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for data warehousing and analytics?',
        'choices': [
            'Amazon Redshift',
            'Amazon DynamoDB',
            'Amazon RDS',
            'Amazon S3'
        ],
        'correct_answer': 'Amazon Redshift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the purpose of AWS Direct Connect?',
        'choices': [
            'Encrypting data in transit between AWS services',
            'Establishing a dedicated network connection between your network and AWS',
            'Managing virtual networks in the cloud',
            'Monitoring AWS resources and applications'
        ],
        'correct_answer': 'Establishing a dedicated network connection between your network and AWS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for scalable, low-latency, and cost-effective gaming experiences?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'Amazon GameLift',
            'Amazon DynamoDB'
        ],
        'correct_answer': 'Amazon GameLift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for managing and automating software deployments?',
        'choices': [
            'Amazon S3',
            'Amazon EC2',
            'AWS CodeDeploy',
            'AWS CodeCommit'
        ],
        'correct_answer': 'AWS CodeDeploy'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides on-demand scalable computing resources?',
        'choices': [
            'Amazon S3',
            'Amazon EC2',
            'Amazon RDS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon EC2'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for monitoring and managing AWS resources and applications?',
        'choices': [
            'Amazon CloudTrail',
            'Amazon CloudFront',
            'Amazon CloudWatch',
            'Amazon CloudFormation'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides scalable, high-performance NoSQL databases?',
        'choices': [
            'Amazon S3',
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon DynamoDB'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for adding machine learning capabilities to your applications?',
        'choices': [
            'Amazon SageMaker',
            'Amazon Aurora',
            'Amazon Neptune',
            'Amazon EKS'
        ],
        'correct_answer': 'Amazon SageMaker'
    },
     {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable relational database service?',
        'choices': [
            'Amazon DynamoDB',
            'Amazon S3',
            'Amazon RDS',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for content storage and distribution?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'Amazon RDS',
            'Amazon CloudFront'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to set up and operate a scalable, fault-tolerant email sending service?',
        'choices': [
            'Amazon SNS',
            'Amazon SES',
            'Amazon SQS',
            'Amazon SWF'
        ],
        'correct_answer': 'Amazon SES'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for creating, deploying, and managing machine learning models?',
        'choices': [
            'Amazon Rekognition',
            'Amazon SageMaker',
            'Amazon Polly',
            'Amazon Transcribe'
        ],
        'correct_answer': 'Amazon SageMaker'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications?',
        'choices': [
            'Amazon SNS',
            'Amazon SQS',
            'Amazon SES',
            'Amazon SWF'
        ],
        'correct_answer': 'Amazon SQS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for real-time communication with globally distributed devices, web, and mobile apps?',
        'choices': [
            'Amazon SNS',
            'Amazon SQS',
            'Amazon SES',
            'Amazon IoT Core'
        ],
        'correct_answer': 'Amazon IoT Core'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, petabyte-scale data warehousing service?',
        'choices': [
            'Amazon Athena',
            'Amazon Redshift',
            'Amazon Glacier',
            'Amazon Elasticsearch Service'
        ],
        'correct_answer': 'Amazon Redshift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for automatically scaling web applications, maintaining performance, and handling varying load levels?',
        'choices': [
            'Amazon CloudWatch',
            'Amazon Route 53',
            'Amazon Elastic Beanstalk',
            'Amazon CloudFront'
        ],
        'correct_answer': 'Amazon Elastic Beanstalk'
    },
      {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed data warehouse solution that allows you to run complex queries on petabytes of structured data?',
        'choices': [
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora',
            'Amazon RDS'
        ],
        'correct_answer': 'Amazon Redshift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is designed for developers to build, test, and deploy serverless applications?',
        'choices': [
            'Amazon EC2',
            'AWS Lambda',
            'Amazon S3',
            'Amazon RDS'
        ],
        'correct_answer': 'AWS Lambda'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for creating and managing encryption keys for your applications?',
        'choices': [
            'Amazon CloudWatch',
            'AWS Key Management Service (KMS)',
            'Amazon Inspector',
            'Amazon Macie'
        ],
        'correct_answer': 'AWS Key Management Service (KMS)'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to automate the deployment, monitoring, and management of containerized applications?',
        'choices': [
            'Amazon EKS',
            'Amazon ECS',
            'Amazon EC2',
            'Amazon Lambda'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is a fully managed relational database that is compatible with MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides fully managed message queues for storing messages as they travel between computers?',
        'choices': [
            'Amazon SQS',
            'Amazon SNS',
            'Amazon SWF',
            'Amazon SES'
        ],
        'correct_answer': 'Amazon SQS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for collecting, analyzing, and visualizing log and metric data from your AWS resources and applications?',
        'choices': [
            'Amazon CloudFront',
            'Amazon CloudWatch',
            'Amazon CloudTrail',
            'Amazon Route 53'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and distributed graph database?',
        'choices': [
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Neptune',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon Neptune'
    },
     {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and serverless data warehouse?',
        'choices': [
            'Amazon Redshift',
            'Amazon Aurora',
            'Amazon DynamoDB',
            'Amazon Athena'
        ],
        'correct_answer': 'Amazon Athena'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for deploying and managing containerized applications at scale?',
        'choices': [
            'Amazon ECS',
            'Amazon EKS',
            'AWS Lambda',
            'Amazon EC2'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service allows you to set up a virtual private cloud (VPC) and control its networking environment?',
        'choices': [
            'Amazon S3',
            'Amazon VPC',
            'Amazon Route 53',
            'Amazon EC2'
        ],
        'correct_answer': 'Amazon VPC'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a scalable and highly available domain name system (DNS) web service?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'Amazon SES',
            'Amazon SQS'
        ],
        'correct_answer': 'Amazon Route 53'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for running code without provisioning or managing servers?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'AWS Lambda',
            'Amazon RDS'
        ],
        'correct_answer': 'AWS Lambda'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for archiving data to low-cost, durable storage?',
        'choices': [
            'Amazon S3 Glacier',
            'Amazon S3 Standard',
            'Amazon EBS',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3 Glacier'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, highly scalable, and secure document database?',
        'choices': [
            'Amazon RDS',
            'Amazon Aurora',
            'Amazon DynamoDB',
            'Amazon DocumentDB'
        ],
        'correct_answer': 'Amazon DocumentDB'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for enabling developers to easily add voice and text chat capabilities to applications?',
        'choices': [
            'Amazon Lex',
            'Amazon Polly',
            'Amazon Transcribe',
            'Amazon Comprehend'
        ],
        'correct_answer': 'Amazon Lex'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed Kubernetes service?',
        'choices': [
            'Amazon EKS',
            'Amazon ECS',
            'AWS Lambda',
            'Amazon EC2'
        ],
        'correct_answer': 'Amazon EKS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for real-time streaming of large datasets?',
        'choices': [
            'Amazon Kinesis',
            'Amazon Redshift',
            'Amazon S3',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon Kinesis'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed graph database service?',
        'choices': [
            'Amazon Neptune',
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift'
        ],
        'correct_answer': 'Amazon Neptune'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for ingesting, processing, and analyzing real-time, streaming data?',
        'choices': [
            'Amazon Kinesis',
            'Amazon Redshift',
            'Amazon S3',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon Kinesis'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is used for building, training, and deploying machine learning models at scale?',
        'choices': [
            'Amazon SageMaker',
            'Amazon Rekognition',
            'Amazon Comprehend',
            'Amazon Polly'
        ],
        'correct_answer': 'Amazon SageMaker'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for easily deploying and managing containers using Docker?',
        'choices': [
            'Amazon ECS',
            'Amazon EKS',
            'AWS Lambda',
            'Amazon EC2'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, in-memory data store service for real-time applications?',
        'choices': [
            'Amazon ElastiCache',
            'Amazon Redshift',
            'Amazon RDS',
            'Amazon DynamoDB'
        ],
        'correct_answer': 'Amazon ElastiCache'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for distributing content with low latency and high transfer speeds?',
        'choices': [
            'Amazon S3',
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon API Gateway'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, serverless data warehouse service?',
        'choices': [
            'Amazon Redshift',
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Athena'
        ],
        'correct_answer': 'Amazon Athena'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service provides a fully managed, scalable data lake solution?',
        'choices': [
            'Amazon S3',
            'Amazon Redshift',
            'Amazon Athena',
            'Amazon Glacier'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and secure log analytics solution?',
        'choices': [
            'Amazon CloudWatch',
            'Amazon CloudFront',
            'Amazon CloudTrail',
            'Amazon Kinesis'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for creating, publishing, maintaining, monitoring, and securing APIs at any scale?',
        'choices': [
            'Amazon S3',
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon API Gateway'
        ],
        'correct_answer': 'Amazon API Gateway'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, scalable, and secure document storage and sharing service?',
        'choices': [
            'Amazon S3',
            'Amazon Glacier',
            'Amazon WorkDocs',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon WorkDocs'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for continuous integration and continuous delivery (CI/CD) of applications?',
        'choices': [
            'Amazon EC2',
            'Amazon ECR',
            'AWS CodePipeline',
            'Amazon ECS'
        ],
        'correct_answer': 'AWS CodePipeline'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed service for running containerized applications at scale?',
        'choices': [
            'Amazon ECS',
            'Amazon EKS',
            'Amazon EC2',
            'AWS Lambda'
        ],
        'correct_answer': 'Amazon ECS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for storing and retrieving any amount of data from anywhere on the web?',
        'choices': [
            'Amazon S3',
            'Amazon Glacier',
            'Amazon RDS',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, serverless database service for applications that require consistent, single-digit millisecond latency at any scale?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Neptune'
        ],
        'correct_answer': 'Amazon DynamoDB'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for sending bulk and transactional emails to customers?',
        'choices': [
            'Amazon SES',
            'Amazon SNS',
            'Amazon SQS',
            'Amazon WorkMail'
        ],
        'correct_answer': 'Amazon SES'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed service for data analytics, visualization, and machine learning?',
        'choices': [
            'Amazon Athena',
            'Amazon QuickSight',
            'Amazon Redshift',
            'Amazon Neptune'
        ],
        'correct_answer': 'Amazon QuickSight'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for highly scalable, fast, and secure file storage in the cloud?',
        'choices': [
            'Amazon S3',
            'Amazon EFS',
            'Amazon Glacier',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon EFS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, scalable, and durable NoSQL database service?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon DocumentDB'
        ],
        'correct_answer': 'Amazon DynamoDB'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for storing and retrieving large objects, such as videos and files, in the cloud?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed service for deploying and scaling web applications and services?',
        'choices': [
            'Amazon EC2',
            'Amazon ECS',
            'Amazon EKS',
            'AWS Elastic Beanstalk'
        ],
        'correct_answer': 'AWS Elastic Beanstalk'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for object storage with a simple web interface to store and retrieve data from anywhere on the web?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, scalable relational database service?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon DocumentDB'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for global content delivery network (CDN) services?',
        'choices': [
            'Amazon S3',
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon CloudWatch'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, scalable, and secure object storage service?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What AWS service is used for building conversational interfaces into any application using voice and text?',
        'choices': [
            'Amazon Lex',
            'Amazon Polly',
            'Amazon Transcribe',
            'Amazon Comprehend'
        ],
        'correct_answer': 'Amazon Lex'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and secure data warehouse solution?',
        'choices': [
            'Amazon Redshift',
            'Amazon Athena',
            'Amazon RDS',
            'Amazon DynamoDB'
        ],
        'correct_answer': 'Amazon Redshift'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for real-time monitoring and logging of AWS resources and applications?',
        'choices': [
            'Amazon CloudTrail',
            'Amazon CloudFront',
            'Amazon CloudWatch',
            'Amazon CloudSearch'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service is a fully managed, scalable, and durable storage service for long-term data archiving?',
        'choices': [
            'Amazon S3 Glacier',
            'Amazon S3 Standard',
            'Amazon EBS',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3 Glacier'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for serverless computing?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'AWS Lambda',
            'Amazon RDS'
        ],
        'correct_answer': 'AWS Lambda'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed service for database backups, point-in-time recovery, and replication?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for running code in response to events and automatically managing the compute resources required?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'AWS Lambda',
            'Amazon RDS'
        ],
        'correct_answer': 'AWS Lambda'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for long-term data retention?',
        'choices': [
            'Amazon S3 Glacier',
            'Amazon S3 Standard',
            'Amazon EBS',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3 Glacier'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for serverless application orchestration and coordination?',
        'choices': [
            'Amazon Step Functions',
            'Amazon SQS',
            'Amazon SWF',
            'Amazon SNS'
        ],
        'correct_answer': 'Amazon Step Functions'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for block storage volumes?',
        'choices': [
            'Amazon EBS',
            'Amazon S3',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon EBS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for analyzing and visualizing logs from AWS resources and applications?',
        'choices': [
            'Amazon CloudWatch',
            'Amazon CloudTrail',
            'Amazon CloudFront',
            'Amazon CloudSearch'
        ],
        'correct_answer': 'Amazon CloudWatch'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed service for relational databases?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for queuing service for distributed applications?',
        'choices': [
            'Amazon SQS',
            'Amazon SNS',
            'Amazon SWF',
            'Amazon API Gateway'
        ],
        'correct_answer': 'Amazon SQS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for object storage?',
        'choices': [
            'Amazon S3',
            'Amazon EBS',
            'Amazon Glacier',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for domain name system (DNS) web service?',
        'choices': [
            'Amazon Route 53',
            'Amazon CloudFront',
            'Amazon CloudWatch',
            'Amazon CloudTrail'
        ],
        'correct_answer': 'Amazon Route 53'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for cold data archiving?',
        'choices': [
            'Amazon S3 Glacier',
            'Amazon S3 Standard',
            'Amazon EBS',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3 Glacier'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for content delivery, API acceleration, and edge computing?',
        'choices': [
            'Amazon CloudFront',
            'Amazon Route 53',
            'Amazon CloudWatch',
            'Amazon CloudTrail'
        ],
        'correct_answer': 'Amazon CloudFront'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for file storage?',
        'choices': [
            'Amazon EFS',
            'Amazon S3',
            'Amazon Glacier',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon EFS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for provisioning, operating, and scaling cloud infrastructure resources?',
        'choices': [
            'Amazon EC2',
            'Amazon S3',
            'Amazon RDS',
            'Amazon VPC'
        ],
        'correct_answer': 'Amazon EC2'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for hot data storage?',
        'choices': [
            'Amazon S3 Standard',
            'Amazon S3 Glacier',
            'Amazon EBS',
            'Amazon EFS'
        ],
        'correct_answer': 'Amazon S3 Standard'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for managed Active Directory in the cloud?',
        'choices': [
            'Amazon Redshift',
            'Amazon RDS',
            'Amazon S3',
            'AWS Directory Service'
        ],
        'correct_answer': 'AWS Directory Service'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for network file storage?',
        'choices': [
            'Amazon EFS',
            'Amazon S3',
            'Amazon Glacier',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon EFS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'What is the AWS service used for fully managed, scalable MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB databases?',
        'choices': [
            'Amazon RDS',
            'Amazon DynamoDB',
            'Amazon Redshift',
            'Amazon Aurora'
        ],
        'correct_answer': 'Amazon RDS'
    },
    {
        'id': str(uuid.uuid4()),
        'question': 'Which AWS service provides a fully managed, scalable, and durable storage service for web hosting and static content delivery?',
        'choices': [
            'Amazon S3',
            'Amazon EFS',
            'Amazon Glacier',
            'Amazon EBS'
        ],
        'correct_answer': 'Amazon S3'
    }
    # Add more questions as needed
]
