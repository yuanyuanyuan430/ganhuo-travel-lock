# Price Verification Workflow

Use when prices, tickets, hotels, transport, packages, or "值不值" decisions affect the plan.

## Verification Rules

- Treat live prices as volatile. Add `截至 YYYY-MM-DD HH:mm` when checked.
- Prefer official or primary channels: 12306 or airline for transport, attraction official channel for tickets, hotel official site or major OTA listing for rooms.
- For hotels, compare only the same date, room type, occupancy, breakfast, tax/fee, and cancellation rule.
- For flights, activities, and packages, include baggage, refund/change rules, seat or time-slot class, and mandatory fees.
- If live lookup is unavailable, give a planning range and mark the exact item `待核验`.

## Evidence Fields

For each current fact, record:

| Field | Meaning |
|---|---|
| `source` | Official source preferred; otherwise authorized OTA/platform. |
| `url_or_app_path` | URL, app page path, public account name, or search query used. |
| `queried_at` | Local time with timezone. |
| `basis` | Date, people count/ages, room type, ticket type, route, or budget filter. |
| `observed_value` | Price/schedule/policy found, or `not available`. |
| `confidence` | High for official/current page, Medium for OTA, Low for indirect pages. |
| `next_action` | Book, compare, wait, call, or user-confirm. |

If a source requires login or blocks access, say what could not be verified and give the safest user action. Do not pretend the value was checked.

## Source Priority

Prefer sources in this order:

1. Official channels: scenic-area site, official app, official WeChat account, railway/airline/airport/metro sites, city weather/emergency authority.
2. Authorized platforms: 12306, airline apps, major OTA pages, hotel brand sites, travel platform product pages.
3. Public guides/reviews: use only for qualitative risk, not exact current price or availability.

For China trips, common search targets:

- Train: `12306 [from] [to] [date]`
- Flight: airline official app/site, airport site, OTA comparison
- Hotels: hotel brand official site plus 1-2 OTA comparisons
- Attractions: official scenic-area site/app/WeChat plus OTA ticket page
- Weather: China Weather, local meteorological bureau, emergency management notices

## Normalize Before Comparing

- Dates and nights.
- Travelers, child age, and ticket category.
- Included/excluded fees.
- Refundability and payment timing.
- Distance to the route's main zone and likely transfer cost.

## Output Table

| Item | Dates/qty | Source | Price seen | Included/excluded | Rule/risk | Action |
|---|---|---|---|---|---|---|
| [hotel/ticket/train] | [date/count] | [source] | [price or 待核验] | [fees/breakfast/baggage] | [refund/slot/weather] | [book/watch/skip] |

## Language

- Say "查到的当前价" only after live verification.
- Say "预算估算" for unverified planning ranges.
- Do not claim cheapest, guaranteed, or lowest-price results unless the checked sources actually prove that narrow claim.
