CLOUD_FUNCTION_NAME=test-gotovo

requirements:
	poetry export --without-hashes --output requirements.txt

pack:
	zip alice_gotovo.zip requirements.txt -r alice_gotovo

deploy: requirements pack
	yc serverless function version create \
	--function-name=$(CLOUD_FUNCTION_NAME) \
	--runtime python37 \
	--entrypoint alice_gotovo.cloud_function.entry \
	--memory 128m \
	--execution-timeout 3s \
	--source-path ./alice_gotovo.zip

clean:
	rm requirements.txt
	rm alice_gotovo.zip
