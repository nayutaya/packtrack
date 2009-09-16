#! ruby -Ku

require "test/unit"
require "open-uri"
require "rubygems"
require "json"
require "yaml"

class JpExpressJsonTest < Test::Unit::TestCase
  def setup
    @base_url = "http://localhost:8080"
  end

  def test_list__1
    url  = @base_url + "/jpexpress/package/list.json"
    url += "?numbers=144856020890"

    json = nil
    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
        json = io.read
      }
    }

    assert_equal(
      YAML.load_file("jpexpress/list__1.yml"),
      JSON.parse(json))
  end
end
