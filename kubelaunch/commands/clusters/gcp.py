
def gcp_commands(self):
    """This functions creates a variety of commands to augment the configuration of Kubernetes on the Google cloud platform.
    """
    lc=self.launch_config
    commands={}
    commands['create_service_account']="gcloud iam service-accounts create "+lc['g_service_account_name']+ " --display-name "+ lc['g_service_account_name']
    commands['create_key']="gcloud iam service-accounts keys create "+self.cwd+"/gcp/"+lc['g_authorization_file'] +" --iam-account "+lc['g_service_account_name']+"@"+lc['g_project']+".iam.gserviceaccount.com"
    commands['get_policy']="gcloud iam service-accounts get-iam-policy "+lc['g_service_account_name']+"@"+lc['g_project']+".iam.gserviceaccount.com --format json > "+self.cwd+"gcp/policy.json"
    commands['set_policy']="gcloud iam service-accounts set-iam-policy "+lc['g_service_account_name']+"@"+lc['g_project']+".iam.gserviceaccount.com "+self.cwd+"/gcp/policy.json"
    commands['login']="gcloud auth login"
    commands['login_sa']="gcloud auth activate-service-account --key-file "+self.cwd+"/gcp/"+ lc['g_authorization_file']
    commands['create_project']="gcloud projects create "+lc['g_project']+" --set-as-default"
    commands['set_project']="gcloud config set project "+lc['g_project']
    commands['set_zone']="gcloud config set compute/zone "+lc['g_zone']
    commands['create']="gcloud container clusters create "+lc['g_cluster_name']+" --num-nodes="+str(lc['g_num_nodes'])+" --machine-type="+lc['g_machine_type']+" --zone="+lc['g_zone']
    commands['get_credentials']="gcloud container clusters get-credentials "+lc['g_cluster_name']
    commands['stop']="gcloud container clusters resize "+lc['g_cluster_name']+" --size=0 --quiet"
    commands['normal_size']="gcloud container clusters resize "+lc['g_cluster_name']+" --size="+str(lc['g_num_nodes'])+" --quiet"
    commands['class_size']="gcloud container clusters resize "+lc['g_cluster_name']+" --size="+str(lc['g_num_nodes_class'])+" --quiet"
    commands['delete']="gcloud container clusters delete "+lc['g_cluster_name']+" --zone="+lc['g_zone']+" --quiet"
    commands['autoscale']="gcloud alpha container clusters update "+lc['g_cluster_name']+" --enable-autoscaling --min-nodes="+str(lc['g_num_nodes'])+" --max-nodes="+str(lc['g_max_nodes'])+" --zone="+lc['g_zone']+" --node-pool=default-pool"
    commands['create_fixedip']="gcloud compute addresses create "+lc['g_fixedip_namespace']+" --region="+lc['g_region']
    commands['describe_fixedip']="gcloud compute addresses describe "+lc['g_fixedip_namespace']+" --region="+lc['g_region']
    commands['delete_forwarding_rule']="gcloud compute forwarding-rules delete forwarding_rule --quiet"
    commands['delete_fixedip']="gcloud compute addresses delete "+lc['g_fixedip_namespace']+" --region="+lc['g_region']+" --quiet"
    commands['describe_cluster']="gcloud container clusters describe "+lc['g_cluster_name']
    #commands['backup_ssh']="mkdir "+self.cwd+"/.ssh &&"+ "cp ~/.ssh/id_rsa "+self.cwd+"/.ssh/id_rsa_"+lc['cluster_name']+"&& cp ~/.ssh/id_rsa.pub "+self.cwd+"/.ssh/id_rsa_"+lc['cluster_name']+".pub"
    return commands
