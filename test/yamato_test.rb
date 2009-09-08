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
    url  = "http://localhost:8080/yamato/package/list.json"
    url += "?numbers=1,2,3"

    json = nil
    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
        json = io.read
      }
    }

    expected = {
      "request" => {
        "numbers" => ["1", "2", "3"],
      },
    }
    assert_equal(expected, JSON.parse(json))
  end
end
