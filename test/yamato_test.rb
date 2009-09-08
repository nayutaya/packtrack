#! ruby -Ku

require "test/unit"
require "open-uri"

class JsonTest < Test::Unit::TestCase
  def setup
    # nop
  end

  def test_get
    url = "http://localhost:8080/yamato/package/list.json"

    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
      }
    }
  end
end
