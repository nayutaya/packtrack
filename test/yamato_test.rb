#! ruby -Ku

require "test/unit"
require "open-uri"
require "rubygems"
require "json"
require "yaml"

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

    expected = YAML.load_file("yamato/list__1.yml")

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

    expected = YAML.load_file("yamato/list__2.yml")

    #File.open("out.txt", "wb") { |file| file.write(json) }
    assert_equal(expected, JSON.parse(json))
  end
end
