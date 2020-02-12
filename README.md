# DevOps
A project to play with devops tooling

## Dependencies
* Docker
* Docker-Compose
* Python 3.7

## Current Stack
* Flask (Frontend)
    * [localhost:5000](localhost:5000)
* Redis (Caching)
* Docker (Container)
* Docker-Compose (Container Orchestration)
* Portainer (Container Dashboard)
    * [localhost:9000](localhost:9000)
* CircleCI

## Development

Change directories to root and run
```
docker-compose build && docker-compose up
```

The following urls are available:
* [Flask Frontend](localhost:5000)
* [Portainer](localhost:9000)

## Testing

Change directories to root and run
```
pytest
```