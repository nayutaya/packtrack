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

    json = get_json(url)

    assert_equal(
      YAML.load_file("jpexpress/list__1.yml"),
      JSON.parse(json))
  end

  def test_list__2
    url  = @base_url + "/jpexpress/package/list.json"
    url += "?numbers=348001739212,348001786042"

    json = get_json(url)

    assert_equal(
      YAML.load_file("jpexpress/list__2.yml"),
      JSON.parse(json))
  end

  private

  def get_json(url)
    assert_nothing_raised {
      open(url) { |io|
        assert_equal("text/javascript", io.content_type)
        return io.read
      }
    }
  end
end
