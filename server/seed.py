from server.app import db, create_app
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Create Guests
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Taylor Swift", occupation="Singer")
    guest3 = Guest(name="Elon Musk", occupation="CEO")

    db.session.add_all([guest1, guest2, guest3])

    # Create Episodes
    ep1 = Episode(date=date(2023, 10, 1), number=101)
    ep2 = Episode(date=date(2023, 10, 2), number=102)

    db.session.add_all([ep1, ep2])
    db.session.commit()

    # Create Appearances
    a1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    a2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep1.id)
    a3 = Appearance(rating=3, guest_id=guest3.id, episode_id=ep2.id)

    db.session.add_all([a1, a2, a3])
    db.session.commit()

    print("✅ Done seeding!")
