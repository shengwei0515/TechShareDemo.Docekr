IMAGE_NAME = docker.io/smallseal/mock-backend-demo
IMAGE_TAG = $(shell git symbolic-ref --short HEAD)

.PHONY : build

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) -f dockerfile.release .

push:
	docker push $(IMAGE_NAME):$(IMAGE_TAG)

run: 
	docker run --rm -d \
		--name mock-backend \
		-v ${PWD}/demo_data/static/:/root/src/app/static/ \
		-p 5000:5000 \
		$(IMAGE_NAME):$(IMAGE_TAG) 
	docker logs mock-backend -f