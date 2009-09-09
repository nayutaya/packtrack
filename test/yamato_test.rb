#! ruby -Ku

require "test/unit"
require "open-uri"
require "rubygems"
require "json"

class JsonTest < Test::Unit::TestCase
  def setup
    # nop
  end

  def test_list__1
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
      "success"   => true,
      "parameter" => {
        "callback" => nil,
        "numbers"  => ["249711710883"],
      },
      "result"    => {
        "249711710883" => {
          "message"            => "このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
          "type"               => "宅急便",
          "current_state"      => "配達完了",
          "current_state_time" => "2009-08-24 11:19",
          "detail"             => {
            "delivery_time" => "08/24",
          },
          "history"            => [
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

    #File.open("out.txt", "wb") { |file| file.write(json) }
    assert_equal(expected, JSON.parse(json))
  end

  def test_list__2
    url  = "http://localhost:8080"
    url += "/yamato/package/list.json"
    url += "?numbers=099723653466,203115515466"

    json = nil
    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
        json = io.read
      }
    }

    expected = {
      "success"   => true,
      "parameter" => {
        "callback" => nil,
        "numbers"  => ["099723653466", "203115515466"],
      },
      "result"    => {
        "099723653466" => {
          "message"            => "このお品物はお届けが済んでおります。",
          "type"               => "クロネコメール便",
          "current_state"      => "投函完了",
          "current_state_time" => "2009-07-09 11:22",
          "detail"             => {
            "delivery_time" => nil,
          },
          "history"            => [
            {
              "state"        => "発送",
              "time"         => "2009-07-07 20:12",
              "station_name" => "奈良物流システム支店",
              "station_code" => "064600",
            },
            {
              "state"        => "投函完了",
              "time"         => "2009-07-09 11:22",
              "station_name" => "豊田上郷センターＭ",
              "station_code" => "357171",
            },
          ],
        },
        "203115515466" => {
          "message"            => "このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
          "type"               => "宅急便コレクト（クール）",
          "current_state"      => "配達完了",
          "current_state_time" => "2009-07-02 20:43",
          "detail"             => {
            "delivery_time" => "20:00-21:00",
          },
          "history"            => [
            {
              "state"        => "荷物受付",
              "time"         => "2009-07-01 14:24",
              "station_name" => "徳島物流システム営業所",
              "station_code" => "082600",
            },
            {
              "state"        => "発送",
              "time"         => "2009-07-01 14:24",
              "station_name" => "徳島物流システム営業所",
              "station_code" => "082600",
            },
            {
              "state"        => "配達完了",
              "time"         => "2009-07-02 20:43",
              "station_name" => "光明センター",
              "station_code" => "060191",
            },
          ],
        },
      },
    }

    #File.open("out.txt", "wb") { |file| file.write(json) }
    assert_equal(expected, JSON.parse(json))
  end
end
