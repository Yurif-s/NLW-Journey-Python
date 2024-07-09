import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interacao com o banco')
def test_registry_link():
   conn = db_connection_handler.get_connection()
   links_repository = LinksRepository(conn)

   links_infos = {
      "id": link_id,
      "trip_id": trip_id,
      "link": "example.com",
      "title": "exampleTitle"
   }

   links_repository.registry_links(links_infos)

@pytest.mark.skip(reason='interacao com o banco')
def test_find_links_from_trip():
   conn = db_connection_handler.get_connection()
   links_repository = LinksRepository(conn)

   reponse = links_repository.find_link_from_trip(trip_id)
   print()
   print(reponse)