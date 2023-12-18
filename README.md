<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
-->
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Project Dependencies">Project Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Data Ingestion">Data Ingestion</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
### Built With

- [Apache Kafka](https://kafka.apache.org/): Apache Kafka is an event streaming platform that captures data in real-time from various sources like databases, sensors, mobile devices, and more. This platform stores event streams durably, processes and reacts to streams in real-time, and routes them to various destinations.

- [AWS MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html): MSK Connect is a feature of Amazon MSK designed to streamline data streaming to and from Apache Kafka clusters. Built-in connectors enable easy data movement to popular data stores like Amazon S3.

- [AWS MSK (Amazon Managed Streaming for Apache Kafka)](https://aws.amazon.com/msk/): Amazon MSK is a fully managed service for Apache Kafka that allows the creation and operation of applications using Apache Kafka to process streaming data. More information can be found in the [developer guide](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html).


- [Kafka REST Proxy](https://docs.confluent.io/platform/current/kafka-rest/index.html): The Confluent REST Proxy provides a RESTful interface to an Apache Kafka cluster, simplifying message production, consumption, cluster state viewing, and administrative actions.

- [PySpark](https://spark.apache.org/docs/3.4.1/api/python/index.html): PySpark is the Python API for Apache Spark, enabling real-time, large-scale data processing in a distributed environment using Python. It provides a Python-based shell for interactive data analysis.


- [AWS API Gateway](https://aws.amazon.com/api-gateway/): Amazon API Gateway is a fully managed service facilitating the creation, publication, maintenance, monitoring, and securing of APIs. It acts as the primary interface for applications to access backend services.

- [Apache Spark](https://spark.apache.org/docs/3.4.1/): Apache Spark™ is a multi-language engine for executing data engineering, data science, and machine learning tasks across single-node machines or clusters. It supports various high-level APIs and tools for different data processing needs.


- [Databricks](https://docs.databricks.com/en/index.html): Databricks is a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale. It integrates with cloud storage, security, and manages cloud infrastructure.

- [AWS Kinesis](https://aws.amazon.com/kinesis/): AWS Kinesis is a managed service for processing and analyzing streaming data. Kinesis Data Streams temporarily store data before processing it using Spark on Databricks for stream analysis.

- [Managed Workflows for Apache Airflow (MWAA)](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html): MWAA leverages Apache Airflow to build scheduling workflows for batch-oriented processes. It abstracts infrastructure management, offering scalability, availability, and security.





<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Project Description
In the ever-evolving landscape of digital platforms, harnessing the power of data analytics is paramount to enhancing user experiences and providing tailored, valuable content. Pinterest, a prominent social media platform, exemplifies this by constantly analyzing billions of data points daily to refine their user offerings. This wealth of data empowers Pinterest to make informed decisions, optimize user engagement, and ensure a more personalized experience for its users.

In this project, we embark on a journey to replicate the data-driven success of Pinterest by constructing a similar data processing and analytics system. Our focus is to leverage the expansive capabilities of the AWS Cloud, a robust and flexible cloud computing platform, to achieve this objective. By harnessing the scalability, storage, and computational power of AWS, we aim to create a system capable of ingesting and processing vast quantities of data, extracting valuable insights, and enhancing user experiences.

The core mission of this project is to empower businesses and organizations to harness the potential of their data. Through the implementation of cloud-based solutions, we will design and deploy a data infrastructure that can efficiently manage data ingestion, storage, processing, and analysis. By doing so, we aim to enable our users to make data-driven decisions, optimize their offerings, and, ultimately, enhance the value they provide to their customers.

This project encompasses a comprehensive journey through the AWS Cloud, covering various key services and components, including data storage, data processing, and analytics. We will explore the AWS ecosystem to create a system that allows for data crunching at scale, similar to what Pinterest has mastered. Through this exploration, we hope to equip you with the knowledge and skills to build your own data-driven systems on the AWS Cloud.

Join us on this exciting expedition into the world of data analytics and cloud computing as we replicate Pinterest's data-driven success using the AWS Cloud. Together, we will embark on a transformative journey of data exploration, analysis, and value creation.
 
## Project Dependencies
In order to run this project successfully , the following modules need to be installed:

- `python-dotenv`
- `sqlalchemy`
- `requests`

If you are using Anaconda and virtual environments (which is recommended), you can clone the Conda environment by executing the following command. Ensure that the 'env.yml' file is present within the project directory:

```bash
conda env create -f env.yml -n $ENVIRONMENT_NAME
```

<!-- the data -->
## The Data

To replicate the data environment typically encountered by Pinterest engineers, this project includes a script, [user_posting_emulation_to_console.py](user_posting_scripts/user_posting_emulation_to_console.py), that mimics a stream of random data points received by the Pinterest API when users make POST requests to upload data to Pinterest.

When executed, this script initializes a database connector class that connects to an AWS RDS database housing three key tables:

- `pinterest_data`: Contains information about posts uploaded to Pinterest.
- `geolocation_data`: Stores geolocation data associated with each Pinterest post found in the `pinterest_data` table.
- `user_data`: Holds user-related information for each post found in the `pinterest_data` table.

The `run_infinite_post_data_loop()` method operates infinitely at random intervals ranging between 0 and 2 seconds. It selects all columns of a randomly chosen row from each table, capturing the data into respective dictionaries. These three dictionaries are then displayed on the console.

Here are examples of the generated data:

**pinterest_data:**
```plaintext
{'index': 7528, 'unique_id': 'fbe53c66-3442-4773-b19e-d3ec6f54dddf', 'title': 'No Title Data Available', 'description': 'No description available Story format', 'poster_name': 'User Info Error', 'follower_count': 'User Info Error', 'tag_list': 'N,o, ,T,a,g,s, ,A,v,a,i,l,a,b,l,e', 'is_image_or_video': 'multi-video(story page format)', 'image_src': 'Image src error.', 'downloaded': 0, 'save_location': 'Local save in /data/mens-fashion', 'category': 'mens-fashion'}

geolocation_data:
{'ind': 7528, 'timestamp': datetime.datetime(2020, 8, 28, 3, 52, 47), 'latitude': -89.9787, 'longitude': -173.293, 'country': 'Albania'}

user_data:
{'ind': 7528, 'first_name': 'Abigail', 'last_name': 'Ali', 'age': 20, 'date_joined': datetime.datetime(2015, 10, 24, 11, 23, 51)}
```

geolocation_data:
```
{'ind': 7528, 'timestamp': datetime.datetime(2020, 8, 28, 3, 52, 47), 'latitude': -89.9787, 'longitude': -173.293, 'country': 'Albania'}
```

user_data:
```
{'ind': 7528, 'first_name': 'Abigail', 'last_name': 'Ali', 'age': 20, 'date_joined': datetime.datetime(2015, 10, 24, 11, 23, 51)}
```

<!-- Building the pipeline -->
## Building the pipeline
The initial phase of our data pipeline involves setting up an Apache Kafka cluster within the AWS cloud ecosystem, leveraging Amazon Managed Streaming for Apache Kafka (MSK). This getting started guide offered by AWS serves as a valuable resource. Below, I outline the steps for launching a cluster:

1. Sign in to the AWS console and access MSK through the 'Services' menu.
2. Within the MSK console, initiate the cluster creation process by selecting 'Create cluster.'
3. Choose between 'Quick' or 'Custom' setup options and assign a name to the cluster.

4. Scroll down and choose 'Provisioned' and specify the Kafka version and broker type. The type chosen will depend on requirements and cost considerations.

5. Finally, scroll down and click 'Create cluster'. The cluster can take between 15 and 20 minutes to create. When the cluster has been created, navigate to the 'Properties' tab, locate the network settings and take a note of the security group associated with the cluster. Next, click on 'View client information' and take a note of the bootstrap servers.

Once the cluster is up and running, a client is needed to communicate with it. In this project, an EC2 instance is used to act as the client.

1. Navigate to the EC2 dashboard and click on 'Launch Instance':

2. Give the instance a name, e.g. 'pinterest-kafka-client'.
3. Keep the default Application and OS images, and instance type. Again, this choice may be determined by usage and cost considerations.

4. Create a new keypair for connecting securely to the instance via SSH. Give the keypair a descriptive name and choose 'RSA' and '.pem' for the type and file format, respectively. The .pem file will automatically download - keep this file safe for later use.

5. Keep the default settings for the other sections. Click on 'Launch Instance' in the right-hand summary menu.

### Enable client machine to connect to the cluster
For the client machine to establish a connection with the cluster, it's essential to modify the inbound rules within the associated security group.

1. Access the EC2 dashboard and navigate to 'Security Groups' in the left-hand menu.
2. Choose the security group linked with the Kafka cluster (noted previously).
3. Click on the 'Inbound rules' tab and select 'Edit inbound rules.'
4. Add a new rule by clicking 'Add rule'. Opt for 'All traffic' as the type and select the security group connected to the EC2 instance.
5. Save the updated rules.

Additionally, creating an IAM role for the client machine is necessary:

1. Visit the AWS IAM dashboard and select 'Roles' from the left-hand menu, then click 'Create role'.
2. Choose 'AWS service' followed by 'EC2', and proceed by clicking 'Next'.
3. Select 'Create policy' on the subsequent page.
4. In the policy editor, opt for JSON format and paste the provided policy below. 
Note: This policy may be overly permissive; in a production environment, consider a more restricted policy.

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "kafka:ListClustersV2",
                "kafka:ListVpcConnections",
                "kafka:DescribeClusterOperation",
                "kafka:GetCompatibleKafkaVersions",
                "kafka:ListClusters",
                "kafka:ListKafkaVersions",
                "kafka:GetBootstrapBrokers",
                "kafka:ListConfigurations",
                "kafka:DescribeClusterOperationV2"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "kafka-cluster:*",
            "Resource": [
                "arn:aws:kafka:*:<AWS-UUID>:transactional-id/*/*/*",
                "arn:aws:kafka:*:<AWS-UUID>:group/*/*/*",
                "arn:aws:kafka:*:<AWS-UUID>:topic/*/*/*",
                "arn:aws:kafka:*:<AWS-UUID>:cluster/*/*"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "kafka:*",
            "Resource": [
                "arn:aws:kafka:*:<AWS-UUID>:cluster/*/*",
                "arn:aws:kafka:*:<AWS-UUID>:configuration/*/*",
                "arn:aws:kafka:*:<AWS-UUID>:vpc-connection/*/*/*"
            ]
        }
    ]
}
```
To grant necessary permissions to the EC2 instance, follow these steps:

5. On the IAM dashboard, create a new policy in JSON format and save it.
6. Navigate back to the 'Create role' tab, refresh the page, and select the newly     created policy.
7. Continue by naming and saving the role.
8. Head to the EC2 dashboard and select the relevant client instance.
9. Under 'Actions' and 'Security', choose 'Modify IAM role'.
10. Select the recently created role and confirm by clicking 'Update IAM role'.

### Install Kafka on the client machine
1. Once the new instance is in the running state, connect via SSH to interact with the instance using the command line. To do this, click on the instance ID to open the summary page, then click on 'Connect':

2. Follow the instructions in the 'SSH' tab to connect to the instance.

```bash
# make sure key is not publicly viewable
chmod 400 pinterest-kafka-client-keypair.pem
# connect
ssh -i "pinterest-kafka-client-keypair.pem" ec2-user@<instance-public-DNS>
```

3. Now on the instance command line:

```bash
# install Java - required for Kafka to run
sudo yum install java-1.8.0
# download Kafka - must be same version as MSK cluster created earlier
wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz
# unpack .tgz
tar -xzf kafka_2.12-2.8.1.tgz
```

4. Install the [MSK IAM package](https://github.com/aws/aws-msk-iam-auth) that will enable the MSK cluster to authenticate the client:

```bash
# navigate to the correct directory
cd kafka_2.12-2.8.1/libs/
# download the package
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.5/aws-msk-iam-auth-1.1.5-all.jar
```

5. Configure the client to be able to use the IAM package:

```bash
# open bash config file
nano ~/.bashrc
```

Add the following line to the config file, then save and exit:

```bash
export CLASSPATH=/home/ec2-user/kafka_2.12-2.8.1/libs/aws-msk-iam-auth-1.1.5-all.jar
```

Continue with configuration:

```bash
# activate changes to .bashrc
source ~/.bashrc
# navigate to Kafka bin folder
cd ../bin
# create client.properties file
nano client.properties
```

Add the following code to the client.properties file, then save and exit:

```bash
# Sets up TLS for encryption and SASL for authN.
security.protocol = SASL_SSL

# Identifies the SASL mechanism to use.
sasl.mechanism = AWS_MSK_IAM

# Binds SASL client implementation.
sasl.jaas.config = software.amazon.msk.auth.iam.IAMLoginModule required;

# Encapsulates constructing a SigV4 signature based on extracted credentials.
# The SASL client bound by "sasl.jaas.config" invokes this class.
sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler
```
## Kafka Topics and Message Delivery

Once your Kafka cluster is set up and running, it's crucial to establish topics for data ingestion and manage message delivery.

### Creating Topics

Topics can be established on the Kafka cluster using the command line on your client machine. Utilize the following command, replacing `<BootstrapServerString>` with the noted bootstrap server string from cluster creation:

```bash
<path-to-your-kafka-installation>/bin/kafka-topics.sh --create --bootstrap-server <BootstrapServerString> --command-config client.properties --topic <topic name>
```
For this project, three topics were created—pinterest_data, geolocation_data, and user_data.

### Streaming via REST API
To facilitate data delivery to the Kafka cluster, I leveraged the Confluent package to set up a REST API on the client, allowing interaction with the Kafka cluster.

Begin by downloading the Confluent package on your client's command line:
```bash
# download the package
sudo wget https://packages.confluent.io/archive/7.2/confluent-7.2.0.tar.gz
# extract the files
tar -xvzf confluent-7.2.0.tar.gz 
```

After downloading, navigate to the kafka-rest.properties file:
```bash
# go to the directory
cd confluent-7.2.0/etc/kafka-rest/
nano kafka-rest.properties
```
Modify this configuration file according to your requirements. This REST API facilitates interaction with the Kafka cluster, enabling seamless data streaming and retrieval.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
<!-- CONTACT -->
## Contact

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments