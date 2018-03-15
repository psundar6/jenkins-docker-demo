import route53

### include . after the domain name!
hosted_zone_name='www.aoroute53.com.'


running_instances = [('18.188.87.216','us-east-2'),('184.169.192.17','us-west-1')]
#print "ip addr: ", instance[0]
#print "region: ", instance[1]

####################################
## enter AWS API credentials
####################################
connection = route53.connect(
    aws_access_key_id='AKIAJLI2ZIBDVQVY43CA',
    aws_secret_access_key='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',
)


#########################################
## list all hosted zones in AWS/Route 53
#########################################

for zone in connection.list_hosted_zones():
    # You can then do various things to the zone.
    print(zone.name)

###########################################################
## create a record set for the hosted zone
###########################################################
## ip addr1 = 18.188.87.216 Ohio region
## ip addr2 = 184.169.192.17 N.Cal region

for instance in running_instances:
        print "ip address: ",instance[0]
        print "region: ",instance[1]
        str1 = "from script: route to %s" % (instance[1])
	new_record, change_info = zone.create_a_record(
   	 name=hosted_zone_name,
    	# A list of IP address entries, in the case fo an A record.
   	 values=[instance[0]],
   	 ttl='30',
   	 region=instance[1],
         set_identifier=str1,
	)

for record_set in zone.record_sets:
    if record_set.name == hosted_zone_name:
        print(record_set)
        # Stopping early may save some additional HTTP requests,
        # since zone.record_sets is a generator.
