

import boto3
import json

files_to_ignore = [ "README.md" ]
codecommit_client = boto3.client('codecommit')
codepipeline_client = boto3.client('codepipeline')

def lambda_handler(event, context):
    old_commit_id = event["detail"]["oldCommitId"]
    new_commit_id = event["detail"]["commitId"]
    # Get commit differences
    codecommit_response = codecommit_client.get_differences(
        repositoryName="finiquitos",
        beforeCommitSpecifier=str(old_commit_id),
        afterCommitSpecifier=str(new_commit_id)
    )
    
    print("LDCV differences: " + str(codecommit_response["differences"]))
    # Search commit differences for files to ignore
    for difference in codecommit_response["differences"]:
        file_name = difference["afterBlob"]["path"].lower()
        
        # If and only if changes are found in gs-spring-boot/complete, trigger the codepipeline. 
        # Else, dont do anything.
        if file_name.startswith('fuentes/web/backend'):
            codepipeline_response = codepipeline_client.start_pipeline_execution(
                name="Prefiniquitos-Backend"
                )
            # Break to avoid executing the pipeline twice
            break
        if file_name.startswith('fuentes/web/frontend'):
            codepipeline_response = codepipeline_client.start_pipeline_execution(
                name="Prefiniquitos-Frontend"
                )
            # Break to avoid executing the pipeline twice
            break
        if file_name.startswith('fuentes/cron-depurar'):
            codepipeline_response = codepipeline_client.start_pipeline_execution(
                name="Prefiniquitos-Function"
                )
            # Break to avoid executing the pipeline twice
            break
        
    
    return {
        'message': 'success'
    }
