# NAMESPACED
v1                            --  Binding
v1                            --  ConfigMap
v1                            --  Endpoints
v1                            --  Event
v1                            --  LimitRange
v1                            --  PersistentVolumeClaim
v1                            --  Pod
v1                            --  PodTemplate
v1                            --  ReplicationController
v1                            --  ResourceQuota
v1                            --  Secret
v1                            --  ServiceAccount
v1                            --  Service
apps/v1                       --  ControllerRevision
apps/v1                       --  DaemonSet
apps/v1                       --  Deployment
apps/v1                       --  ReplicaSet
apps/v1                       --  StatefulSet
authorization.k8s.io/v1       --  LocalSubjectAccessReview
autoscaling/v1                --  HorizontalPodAutoscaler
batch/v1                      --  CronJob
batch/v1                      --  Job
coordination.k8s.io/v1        --  Lease
discovery.k8s.io/v1           --  EndpointSlice
events.k8s.io/v1              --  Event
extensions/v1beta1            --  Ingress
networking.k8s.io/v1          --  Ingress
networking.k8s.io/v1          --  NetworkPolicy
policy/v1                     --  PodDisruptionBudget
rbac.authorization.k8s.io/v1  --  RoleBinding
rbac.authorization.k8s.io/v1  --  Role
storage.k8s.io/v1beta1        --  CSIStorageCapacity

# NOT NAMESPACED
v1                                    --  ComponentStatus
v1                                    --  Namespace
v1                                    --  Node
v1                                    --  PersistentVolume
admissionregistration.k8s.io/v1       --  MutatingWebhookConfiguration
admissionregistration.k8s.io/v1       --  ValidatingWebhookConfiguration
apiextensions.k8s.io/v1               --  CustomResourceDefinition
apiregistration.k8s.io/v1             --  APIService
authentication.k8s.io/v1              --  TokenReview
authorization.k8s.io/v1               --  SelfSubjectAccessReview
authorization.k8s.io/v1               --  SelfSubjectRulesReview
authorization.k8s.io/v1               --  SubjectAccessReview
certificates.k8s.io/v1                --  CertificateSigningRequest
flowcontrol.apiserver.k8s.io/v1beta1  --  FlowSchema
flowcontrol.apiserver.k8s.io/v1beta1  --  PriorityLevelConfiguration
networking.k8s.io/v1                  --  IngressClass
node.k8s.io/v1                        --  RuntimeClass
policy/v1beta1                        --  PodSecurityPolicy
rbac.authorization.k8s.io/v1          --  ClusterRoleBinding
rbac.authorization.k8s.io/v1          --  ClusterRole
scheduling.k8s.io/v1                  --  PriorityClass
storage.k8s.io/v1                     --  CSIDriver
storage.k8s.io/v1                     --  CSINode
storage.k8s.io/v1                     --  StorageClass
storage.k8s.io/v1                     --  VolumeAttachment