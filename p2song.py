# NOT IN USE SAMPLE CODE

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=10,
        playlistId="PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()




"""
{
  "kind": "youtube#playlistItemListResponse",
  "etag": "-5w1LPq4VlBTuNipbiWoruKYF-Q",
  "nextPageToken": "EAAaBlBUOkNBbw",
  "items": [
    {
      "kind": "youtube#playlistItem",
      "etag": "dyIVZtPEKxywIslciUUKFshOg34",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC41NkI0NEY2RDEwNTU3Q0M2",
      "snippet": {
        "publishedAt": "2020-04-20T14:30:19Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "Fly Me To The Moon (Cover) by The Macarons Project",
        "description": "Fly Me To The Moon (Cover)\nPerformed by Frank Sinatra - Written by Bart Howard\nhttps://youtu.be/ZEcqHA7dbwM\n\nListen NOW on Spotify: https://goo.gl/Fpwk7j\n\nGet it on iTunes: https://goo.gl/jNRJTx\nDeezer: https://goo.gl/uFStg9\n\n\n\nLeaving On A Jet Plane - John Denver (Cover) https://youtu.be/rCmcgn793hs\nTonight You Belong to Me (Cover Lyric Video) https://youtu.be/oUNWgZsEsUU\nTelephone - Mocca (Cover) https://youtu.be/swAVXNBw2Sg\nThe Scientist - Coldplay (Cover) by The Macarons Project https://youtu.be/perJHQfO_lA\nSomewhere over The Rainbow (Cover Lyric Video) https://youtu.be/qLu1ETj2kwM\nLike a Star - Corinne Bailey Rae (Cover) https://youtu.be/P2WjwotFBSo\nCreep - Radiohead (Cover) https://youtu.be/dZlHA-KsyI8\nPhotograph - Ed Sheeran (Cover) https://youtu.be/aRxE1barzwk\n\n\nThe Macarons Project\n\nRee\nDito\n\n\n\nLearn the Guitar Chords: https://youtu.be/SZxYfUpwYf4\n\nDukung di KARYAKARSA:\nhttps://karyakarsa.com/themacaronsproject\n\n\n\nSupport us on Ko-fi: \nhttps://ko-fi.com/A6843UFY\n\nMerchandise:\nIndonesia: https://tees.co.id/stores/TheMacaronsProject/\nUS & other location: https://teespring.com/stores/the-macarons-project\n\n\nFollow us on Instagram:\nhttps://www.instagram.com/themacaronsproject/\nLike us on Facebook:\nhttps://www.facebook.com/themacaronsproject\nSoundCloud:\nhttps://soundcloud.com/the-macarons-project\n\n\n2017\n\n#TheMacaronsProject\n#FlyMetoTheMoon\n#FrankSinatra\n#BartHoward\n#Covers",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Ev_-gOW-gMo/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Ev_-gOW-gMo/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Ev_-gOW-gMo/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/Ev_-gOW-gMo/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/Ev_-gOW-gMo/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 0,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "Ev_-gOW-gMo"
        },
        "videoOwnerChannelTitle": "The Macarons Project",
        "videoOwnerChannelId": "UCgOqnJrRvoLd8wuaszFoV-Q"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "w07jqZbNNXgSfHE_bbQqvGnLQBs",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC4yODlGNEE0NkRGMEEzMEQy",
      "snippet": {
        "publishedAt": "2021-01-21T07:28:03Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(FREE) Lofi Type Beat - I'm fine (prod. yusei ft. lul patchy)",
        "description": "Purchase beats: https://www.beatstars.com/yuseiworld/tracks\n\nSERIOUS INQUIRIES ONLY: william.bands12@gmail.com\nhttps://twitter.com/junkiewill\nhttps://www.instagram.com/yuseiworld/\n\nLul Patchy Channel: https://www.youtube.com/channel/UCm_JFsEm0AHvMOUdwDlkUQw\n\nLofi Type Beat\n\nIF ANY ISSUE WITH THE VISUALS BEING USED PLEASE CONTACT ME VIA MY EMAIL OR SOCIAL MEDIAS LISTED ABOVE\n\nOFFICIAL SPOTIFY: https://open.spotify.com/artist/0K3Jtj8PRdPfgYLua8X1dv\n\nOFFICIAL APPLE MUSIC: https://music.apple.com/us/artist/yusei/1472272328\n\nOFFICIAL SOUNDCLOUD: https://soundcloud.com/user-371535188",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/ddNi33NLHb8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/ddNi33NLHb8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/ddNi33NLHb8/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/ddNi33NLHb8/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/ddNi33NLHb8/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 1,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "ddNi33NLHb8"
        },
        "videoOwnerChannelTitle": "Yusei",
        "videoOwnerChannelId": "UC2UL6SD7NG6fnvDXB36r7Nw"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "JYosfID-WPq7baLciJz9rl1ob4w",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC4wMTcyMDhGQUE4NTIzM0Y5",
      "snippet": {
        "publishedAt": "2021-01-21T07:28:21Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(FREE) Lofi Type Beat - Vibe with me for a minute (prod. Yusei)",
        "description": "Purchase beats: https://www.beatstars.com/yuseiworld/tracks\n\nSERIOUS INQUIRIES ONLY: william.bands12@gmail.com\nhttps://twitter.com/junkiewill\nhttps://www.instagram.com/yuseiworld/\n\nLofi Type Beat \n\nVISUALS BY: muqing0329\n\nALL VISUALS RIGHTS TO muqing0329\n\n(IF ANY ISSUE WITH THE VISUALS BEING USED PLEASE CONTACT ME VIA MY SOCIAL MEDIAS OR EMAIL LISTED ABOVE)\n\nOFFICIAL SPOTIFY: https://open.spotify.com/artist/0K3Jtj8PRdPfgYLua8X1dv\n\nOFFICIAL APPLE MUSIC: https://music.apple.com/us/artist/yusei/1472272328",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/F6TKyB72xQg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/F6TKyB72xQg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/F6TKyB72xQg/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/F6TKyB72xQg/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/F6TKyB72xQg/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 2,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "F6TKyB72xQg"
        },
        "videoOwnerChannelTitle": "Yusei",
        "videoOwnerChannelId": "UC2UL6SD7NG6fnvDXB36r7Nw"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "rBtgxJtjVceGyNYrUQbzeB06OxM",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC41MjE1MkI0OTQ2QzJGNzNG",
      "snippet": {
        "publishedAt": "2021-01-21T07:28:29Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(FREE) Juice WRLD Type Beat - shawty I would die for you (prod. yusei x ydd matt)",
        "description": "Purchase beats: https://www.beatstars.com/yuseiworld/tracks\n\nSERIOUS INQUIRIES ONLY: william.bands12@gmail.com\nhttps://twitter.com/junkiewill\nhttps://www.instagram.com/yuseiworld/\n\nYDD Matt Channel: https://www.youtube.com/channel/UCP8FTyssgAWpo9Z1sDLg0MA\n\nJuice WRLD Type Beat\n\nIF ANY ISSUE WITH THE VISUALS BEING USED PLEASE CONTACT ME VIA MY EMAIL OR SOCIAL MEDIAS LISTED ABOVE\n\nOFFICIAL SPOTIFY: https://open.spotify.com/artist/0K3Jtj8PRdPfgYLua8X1dv\n\nOFFICIAL APPLE MUSIC: https://music.apple.com/us/artist/yusei/1472272328\n\nOFFICIAL SOUNDCLOUD: https://soundcloud.com/user-371535188",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/kK-9D-ynQrM/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/kK-9D-ynQrM/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/kK-9D-ynQrM/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/kK-9D-ynQrM/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/kK-9D-ynQrM/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 3,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "kK-9D-ynQrM"
        },
        "videoOwnerChannelTitle": "Yusei",
        "videoOwnerChannelId": "UC2UL6SD7NG6fnvDXB36r7Nw"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "cI7R4nUTy8Hf-1KcUqy2UArXqGQ",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC4wOTA3OTZBNzVEMTUzOTMy",
      "snippet": {
        "publishedAt": "2021-01-21T07:28:36Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "Deleted video",
        "description": "This video is unavailable.",
        "thumbnails": {},
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 4,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "vXiKW_KcaU0"
        }
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "TQB7ugPZ4K6U2WmoA4nX7LqCsh0",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC4xMkVGQjNCMUM1N0RFNEUx",
      "snippet": {
        "publishedAt": "2021-01-21T07:28:41Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(FREE) Lofi Type Beat - will you wait for me ? (prod. yusei ft. lul patchy)",
        "description": "Purchase Beats: https://www.beatstars.com/yuseiworld/tracks\n\nSERIOUS INQUIRIES ONLY: william.bands12@gmail.com\nhttps://twitter.com/junkiewill\nhttps://www.instagram.com/yuseiworld/\n\nLul Patchy Channel: https://www.youtube.com/channel/UCm_JFsEm0AHvMOUdwDlkUQw\n\nLofi Type Beat\n\nIF ANY ISSUE WITH THE VISUALS BEING USED PLEASE CONTACT ME VIA MY EMAIL OR SOCIAL MEDIAS LISTED ABOVE.\n\nOFFICIAL SPOTIFY: https://open.spotify.com/artist/0K3Jtj8PRdPfgYLua8X1dv\n\nOFFICIAL APPLE MUSIC: https://music.apple.com/us/artist/yusei/1472272328\n\nOFFICIAL SOUNDCLOUD: https://soundcloud.com/user-371535188",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/o1CcJG2WIc8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/o1CcJG2WIc8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/o1CcJG2WIc8/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/o1CcJG2WIc8/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/o1CcJG2WIc8/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 5,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "o1CcJG2WIc8"
        },
        "videoOwnerChannelTitle": "Yusei",
        "videoOwnerChannelId": "UC2UL6SD7NG6fnvDXB36r7Nw"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "EbLpfIT0smDfMTg4JUNhm06amsE",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC41MzJCQjBCNDIyRkJDN0VD",
      "snippet": {
        "publishedAt": "2021-01-23T10:58:32Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "Japanese  Type Beat \"Shenron\"",
        "description": "New anime type beat x logic type beat x chance the rapper type beat\n💰 Purchase Beats | Instant delivery (untagged): https://bsta.rs/e2c7b0b\n✉ Email: info@origamisonic.com\n- Loopkits : https://sellfy.com/origami/\nIg : @gamithekami\n\nThumpnail Art by @vangoathe\nBeats with \" Free\" In the title may be used for non profit use Only ( for ex. soundcloud songs )\n✅ Website:   https://origamibeats.beatstars.com/\n\n🌊Contact Email ⇒ info@origamisonic.com\n🌊 Instagram @Origamibeats\n\nSPOTIFY : https://open.spotify.com/artist/4DgQdXSUFq3rhSRemWvQfN\nItunes , Deezer , Tidal & Apple Music : \nSearch \" Origami Beats Stay wavy  \"\n\n\"Soul City\" - Mac miller x Isaiah rashad x Logic type beat prod origami",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/TtpTfJ8dWGw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/TtpTfJ8dWGw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/TtpTfJ8dWGw/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/TtpTfJ8dWGw/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/TtpTfJ8dWGw/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 6,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "TtpTfJ8dWGw"
        },
        "videoOwnerChannelTitle": "Origami",
        "videoOwnerChannelId": "UCmcF_CZ4oA3MkFdUZ5friXA"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "NVRhKQzDmzY4V6jXub9mHrRUhqg",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC5DQUNERDQ2NkIzRUQxNTY1",
      "snippet": {
        "publishedAt": "2021-01-29T03:24:44Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(HARD) ANIME TYPE BEAT \" BAKUGO \" | Free Type Beat / Instrumental 2020",
        "description": "New anime type beat x logic type beat x chance the rapper type beat\n💰 Purchase | Instant delivery (untagged): https://bsta.rs/b7c04b2d\n✉ Email: info@origamisonic.com\n➕ Subscribe: https://goo.gl/nuUwYw\n✅ Website:   https://origamibeats.beatstars.com/\nAMVS\nBy Jazit J\nThumpnail art by @GOATHE\n🌊Contact Email ⇒ info@origamisonic.com\n\n\n🌊 Instagram @Origamithekami\n\n🌊 Loopkit : https://goo.gl/6B7odW\n\nSPOTIFY : https://open.spotify.com/artist/4DgQdXSUFq3rhSRemWvQfN\nItunes , Deezer , Tidal & Apple Music : \nSearch \" Origami Beats Stay wavy  \"\n\n\"Soul City\" - Mac miller x Isaiah rashad x Logic type beat prod origami",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/e8Rg-XFB_Ik/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/e8Rg-XFB_Ik/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/e8Rg-XFB_Ik/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/e8Rg-XFB_Ik/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/e8Rg-XFB_Ik/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 7,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "e8Rg-XFB_Ik"
        },
        "videoOwnerChannelTitle": "Origami",
        "videoOwnerChannelId": "UCmcF_CZ4oA3MkFdUZ5friXA"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "G1Iyh2cCe1PLCGbjDz_9boCUXSQ",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC45NDk1REZENzhEMzU5MDQz",
      "snippet": {
        "publishedAt": "2021-01-29T03:24:49Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(HARD) ANIME TYPE BEAT \" SAITAMA \" | Free Type Beat / Instrumental 2019",
        "description": "New anime type beat x logic type beat x chance the rapper type beat\n💰 Purchase Beats | Instant delivery (untagged): https://bsta.rs/1fb74d9\n\n✉ Email: info@origamisonic.com\n\n\nBeats with \" Free\" In the title may be used for non profit use Only ( for soundcloud )\n✅ Website:   https://origamibeats.beatstars.com/\n\nANIME EDIT BY : \nWaise\nArthas\nBlue Flash \n\n🌊Contact Email ⇒ info@origamisonic.com\n\n\n🌊 Instagram @Origamibeats\n\nSPOTIFY : https://open.spotify.com/artist/4DgQdXSUFq3rhSRemWvQfN\nItunes , Deezer , Tidal & Apple Music : \nSearch \" Origami Beats Stay wavy  \"\n\n\"Soul City\" - Mac miller x Isaiah rashad x Logic type beat prod origami",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 8,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "EdRBMHpUslk"
        },
        "videoOwnerChannelTitle": "Origami",
        "videoOwnerChannelId": "UCmcF_CZ4oA3MkFdUZ5friXA"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "gYsgXL8s0zvl6oapBU8dda7zxIE",
      "id": "UExXRGh0U2lKUVNkUmZfT2didG5iUEQwVWIwM21ZLXRHWC5GNjNDRDREMDQxOThCMDQ2",
      "snippet": {
        "publishedAt": "2021-01-29T03:24:52Z",
        "channelId": "UCJA_bsjew_uMS6f4mqbaRYg",
        "title": "(HARD) ANIME TYPE BEAT \" SAITAMA \" | Free Type Beat / Instrumental 2019",
        "description": "New anime type beat x logic type beat x chance the rapper type beat\n💰 Purchase Beats | Instant delivery (untagged): https://bsta.rs/1fb74d9\n\n✉ Email: info@origamisonic.com\n\n\nBeats with \" Free\" In the title may be used for non profit use Only ( for soundcloud )\n✅ Website:   https://origamibeats.beatstars.com/\n\nANIME EDIT BY : \nWaise\nArthas\nBlue Flash \n\n🌊Contact Email ⇒ info@origamisonic.com\n\n\n🌊 Instagram @Origamibeats\n\nSPOTIFY : https://open.spotify.com/artist/4DgQdXSUFq3rhSRemWvQfN\nItunes , Deezer , Tidal & Apple Music : \nSearch \" Origami Beats Stay wavy  \"\n\n\"Soul City\" - Mac miller x Isaiah rashad x Logic type beat prod origami",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/EdRBMHpUslk/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "James hamich",
        "playlistId": "PLWDhtSiJQSdRf_OgbtnbPD0Ub03mY-tGX",
        "position": 9,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": "EdRBMHpUslk"
        },
        "videoOwnerChannelTitle": "Origami",
        "videoOwnerChannelId": "UCmcF_CZ4oA3MkFdUZ5friXA"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 28,
    "resultsPerPage": 10
  }
}
"""