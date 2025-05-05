# =========
# CREATE
# =========

# Generate a unique suffix for naming resources

resource "random_id" "suffix" {
  byte_length = 4
}
