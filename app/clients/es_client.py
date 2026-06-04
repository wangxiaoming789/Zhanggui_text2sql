from elasticsearch import AsyncElasticsearch

from app.config.app_config import ESConfig, app_config


class ESClientManager:
    def __init__(self, config: ESConfig):
        self.config = config
        self.client: AsyncElasticsearch | None = None

    def _get_url(self):
        return f"http://{self.config.host}:{self.config.port}"

    def init(self):
        self.client = AsyncElasticsearch(hosts=[self._get_url()])#,request_timeout=100

    async def close(self):
        await self.client.close()


es_client_manager = ESClientManager(app_config.es)


if __name__ == '__main__':
    es_client_manager.init()
    async def test():
        client = es_client_manager.client

        resp =await client.indices.create(
            mappings={
                "dynamic": False,
                "properties": {
                    "name":{
                        "type": "text",
                    },
                    "author":{
                        "type": "text",
                    },
                    "release_date":{
                        "type": "date",
                        "format": "yyyy-mm-dd",
                    },
                    "page_count":{
                        "type": "integer"
                    }
                }
            }
        )

