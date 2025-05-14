# 🧰 Top 20 `gcloud` CLI Commands

Useful commands for managing Google Cloud resources via the `gcloud` CLI.

---

## 🔧 Project & Config

1. `gcloud auth login`  
   Authenticate your account.

2. `gcloud config set project [PROJECT_ID]`  
   Set the active project.

3. `gcloud projects list`  
   List all accessible projects.

4. `gcloud config list`  
   View current config (project, region, etc.).

5. `gcloud services list`  
   List enabled APIs/services for the current project.

6. `gcloud services enable [SERVICE_NAME]`  
   Enable an API (e.g., `compute.googleapis.com`).

---

## ☁️ Compute Engine

7. `gcloud compute instances list`  
   List VM instances.

8. `gcloud compute instances create [NAME] --zone=[ZONE]`  
   Create a new VM.

9. `gcloud compute ssh [INSTANCE_NAME] --zone=[ZONE]`  
   SSH into a VM.

10. `gcloud compute disks list`  
    List persistent disks.

---

## 📦 Cloud Storage

11. `gcloud storage buckets list`  
    List Cloud Storage buckets.

12. `gcloud storage cp [SRC] [DEST]`  
    Upload/download files.  
    Example: `gcloud storage cp file.txt gs://my-bucket/`

13. `gcloud storage ls`  
    List files in a bucket.

---

## 🔐 IAM & Identity

14. `gcloud iam service-accounts list`  
    List service accounts.

15. `gcloud projects get-iam-policy [PROJECT_ID]`  
    View IAM policies.

16. `gcloud projects add-iam-policy-binding [PROJECT_ID]`  
    Add IAM roles for a user or service account.

---

## 🌐 Networking

17. `gcloud compute firewall-rules list`  
    List firewall rules.

18. `gcloud compute addresses list`  
    List static IP addresses.

---

## 🔍 Resource Inspection

19. `gcloud asset search-all-resources --project=[PROJECT_ID]`  
    List all resources in a project (requires Asset Inventory API).

20. `gcloud billing accounts list`  
    View available billing accounts.

---

## 📚 Resources

- [gcloud CLI Reference](https://cloud.google.com/sdk/gcloud/reference)  
- [gcloud Cheat Sheet (PDF)](https://cloud.google.com/sdk/docs/cheatsheet)  
- [Google Cloud Shell](https://shell.cloud.google.com/)