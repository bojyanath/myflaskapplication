# ABOUT YAML SYNTAX FOR WORKFLOWS:


Workflow files use YAML syntax, and must have either a .yml or .yaml file extension


## 
<TABLE>
<TH> NAME :</TH>
<TR>
The name of the workflow. GitHub displays the names of your workflows under your repository's "Actions" tab
</TR>
</TABLE>


## 
<TABLE>
<TH> RUN-NAME :</TH>
<TR>
The name for workflow runs generated from the workflow. GitHub displays the workflow run name in the list of workflow runs on your repository's "Actions" tab
Example run-name: Deploy to ${{ inputs.deploy_target }} by @${{ github.actor }}
</TR>
</TABLE>

## 
<TABLE>
<TH> ON :</TH>
<TR>
To automatically trigger a workflow, use on to define which events can cause the workflow to run.
</TR>
</TABLE>


## 
<TABLE>
<TH> PERMISSIONS :</TH>
<TR>
You can use permissions either as a top-level key, to apply to all jobs in the workflow, or within specific jobs. When you add the permissions key within a specific job, all actions and run commands within that job that use the GITHUB_TOKEN gain the access rights you specify.
</TR>
</TABLE>


## 
<TABLE>
<TH> ENV :</TH>
<TR>
A map of variables that are available to the steps of all jobs in the workflow. You can also set variables that are only available to the steps of a single job or to a single step
</TR>
</TABLE>


## 
<TABLE>
<TH> DEFAULTS :</TH>
<TR>
Use defaults to create a map of default settings that will apply to all jobs in the workflow. You can also set default settings that are only available to a job.
</TR>
</TABLE>

 
## 
<TABLE>
<TH> CONCURRENCY :</TH>
<TR>
Use concurrency to ensure that only a single job or workflow using the same concurrency group will run at a time. A concurrency group can be any string or expression. The expression can only use github, inputs and vars contexts
When a concurrent job or workflow is queued, if another job or workflow using the same concurrency group in the repository is in progress, the queued job or workflow will be pending. Any pending job or workflow in the concurrency group will be canceled. This means that there can be at most one running and one pending job in a concurrency group at any time.
To also cancel any currently running job or workflow in the same concurrency group, specify cancel-in-progress: true. To conditionally cancel currently running jobs or workflows in the same concurrency group, you can specify cancel-in-progress as an expression with any of the allowed expression contexts.
</TR>
</TABLE>



## 
<TABLE>
<TH> JOBS :</TH>
<TR>
A workflow run is made up of one or more jobs, which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the "jobs.(job_id).needs" keyword.Each job runs in a runner environment specified by "runs-on",You can run an unlimited number of jobs as long as you are within the workflow usage limit
</TR>
</TABLE>


## 
<TABLE>
<TH> JOBS.(JOB_ID): </TH>
<TR>
Use " jobs.(job_id) " to give your job a unique identifier. The key job_id is a string and its value is a map of the job's configuration data. You must replace (job_id) with a string that is unique to the jobs object. The (job_id) must start with a letter or _ and contain only alphanumeric characters, -, or _.
</TR>
</TABLE>


##
<TABLE>
<TH> JOBS.(JOBS).STEPS :</TH>
<TR>
A job contains a sequence of tasks called " steps ". Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in S Docker registry. Not all steps run actions, but all actions run as a step. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps. GitHub provides built-in steps to set up and complete a job.
GitHub only displays the first 1,000 checks, however, you can run an unlimited number of steps as long as you are within the workflow usage limits. For more information, see "Usage limits, billing, and administration" for GitHub-hosted runners and "About self-hosted runners" for self-hosted runner usage limits.
</TR>
</TABLE>



## 
<TABLE>
<TH> JOBS.(JOB_ID).SECRETS :</TH>
<TR>
When a job is used to call a reusable workflow, you can use secrets to provide a map of secrets that are passed to the called workflow.
Any secrets that you pass must match the names defined in the called workflow.
</TR>
</TABLE>