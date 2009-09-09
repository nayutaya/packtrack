#! ruby -Ku

require "test/unit"
require "open-uri"
require "rubygems"
require "json"

class JsonTest < Test::Unit::TestCase
  def setup
    # nop
  end

  def test_get
    url  = "http://localhost:8080"
    url += "/yamato/package/list.json"
    url += "?numbers=249711710883"

    json = nil
    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
        json = io.read
      }
    }

    expected = {
      "success" => true,
      "parameter" => {
        "callback" => nil,
        "numbers"  => ["249711710883"],
      },
      "result" => {
        "249711710883" => {
          "message"       => "このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
          "type"          => "宅急便",
          "delivery_time" => "2009-08-24",
          "detail"        => [
            {
              "state"        => "発送",
              "time"         => "2009-08-23 17:44",
              "station_name" => "船橋藤原センター",
              "station_code" => "035012",
            },
            {
              "state"        => "作業店通過",
              "time"         => "2009-08-23 19:37",
              "station_name" => "船橋ベース店",
              "station_code" => "035990",
            },
            {
              "state"        => "配達完了",
              "time"         => "2009-08-24 11:19",
              "station_name" => "日野豊田センター",
              "station_code" => "033092",
            },
          ],
        },
      },
    }

    File.open("out.txt", "wb") { |file| file.write(json) }
    assert_equal(expected, JSON.parse(json))
  end
end
