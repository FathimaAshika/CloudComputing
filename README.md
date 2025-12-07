1- kubectl

2- eksctl 

3 -  aws cli install and configure

4- 
eksctl create cluster --name demo-cluster-1 --region us-east-1 --fargate

5- aws eks update-kubeconfig --name demo-cluster-1 --region us-east-1

6-
eksctl create fargateprofile --cluster demo-cluster-1  --region us-east-1  --name alb-sample-app --namespace game-2048

7-
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/examples/2048/2048_full.yaml

8-// check status 
kubectl get pods -n game-2048 
kubectl get svc  -n game-2048
kubectl get ingress  -n game-2048

9- 
ALB controller setup - pre steps 

eksctl utils associate-iam-oidc-provider --cluster demo-cluster-1 --approve

curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.11.0/docs/install/iam_policy.json

aws iam create-policy  --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy.json


eksctl create iamserviceaccount --cluster=demo-cluster-1  --namespace=kube-system  --name=aws-load-balancer-controller   --role-name AmazonEKSLoadBalancerControllerRole --attach-policy-arn=arn:aws:iam::790117923032:policy/AWSLoadBalancerControllerIAMPolicy --approve

helm repo add eks https://aws.github.io/eks-charts


helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=demo-cluster-1  --set serviceAccount.create=false   --set serviceAccount.name=aws-load-balancer-controller  --set region=us-east-1  --set vpcId=vpc-0d1cc551f8e80bb79


// check the status 
kubectl get deployment -n kube-system aws-load-balancer-controller -w


cloud-computing-bucket-demo // athena // s3 bucket // post hog // 

<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init Rr Mr fi Cr Ar ci Tr Fr capture Mi calculateEventProperties Lr register register_once register_for_session unregister unregister_for_session Hr getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys renderSurvey displaySurvey canRenderSurvey canRenderSurveyAsync identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty Ur jr createPersonProfile zr kr Br opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing Dr debug M Nr getPageViewId captureTraceFeedback captureTraceMetric $r".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('phc_4Eaq6zwPJbaNuaFL7lTVOAxDjBL2wGmPdaddhqgtO5c', {
        api_host: 'https://us.i.posthog.com',
        defaults: '2025-05-24',
        person_profiles: 'identified_only', // or 'always' to create profiles for anonymous users as well
    })
</script>

kubectl rollout restart deployment/deployment-2048 -n game-2048 /// after every image built 

SELECT event, COUNT(*) 
FROM posthog.events
GROUP BY event;



SELECT distinct_id, COUNT(*) AS total_events
FROM posthog.events
GROUP BY distinct_id
ORDER BY total_events DESC
LIMIT 10;


SELECT *
FROM posthog.events
WHERE event = '$pageview'
ORDER BY timestamp DESC
LIMIT 50;




