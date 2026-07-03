---
name: ganhuo-travel-lock
description: Chinese-first travel planning and booking-lock workflow for summer vacation, graduation trips, family trips with children, city recommendations, live ticket/transport/hotel price verification, itinerary lock-in, popular attraction filtering, budgets, pitfalls, and Xiaohongshu-style travel content. Use when the user asks for 旅游攻略, 暑假去哪, 毕业旅行, 带娃旅游, 亲子游, 城市推荐, 热门地点避坑, 小红书旅行攻略, 订票, 查票价, 比价, 酒店价格, 高铁/机票班次, 门票预约, 锁定行程, or similar China-focused trip planning.
---

# Ganhuo Travel Lock

## Workflow

Use this skill to produce practical Chinese travel攻略 and to help lock a trip through live evidence, not guesses.

1. Read `references/travel-guide-template.md` before drafting a guide.
2. Also read `references/booking-lockin-workflow.md` and `references/price-verification-workflow.md` when the request includes 订票, 查价格, 比价, 酒店, 高铁, 机票, 门票预约, 实时, 帮我定下来, 锁定, or any purchase-adjacent decision.
3. Ask at most 3 blocking questions only when these are missing and cannot be inferred: 出发地, 天数/日期, 人群类型. For live booking checks, exact date, party size/ages, and budget can be blocking too; ask only the missing items needed for the lookup.
4. Default soft fields explicitly when missing: 预算中等, 节奏中等, 不自驾, 国内游.
5. If the destination is undecided, recommend only 3 differentiated city/route options.
6. Build the itinerary by area: prefer one main zone per day, with backup indoor/low-effort options for summer heat or rain.
7. For volatile facts, browse or use available live tools when the user asks for current prices, availability, schedules, opening hours, reservations, weather, or hotel policies. Cite source name, URL/app path, and query time.
8. Sort popular places into 保留/跳过/备选 with reasons tied to crowding, weather, child fit, transit friction, budget, and content value.
9. Maintain a lock state when decisions converge: `已锁定`, `待核验`, `备选`, `变更需确认`.

## Boundaries

- Do not invent precise real-time prices, tickets, opening hours, reservation slots, queue times, event schedules, or transport times.
- If live verification is needed and unavailable, mark the item as `待核验` and give the official channel or search target.
- If the user asks to "直接编" volatile information, refuse to fabricate that part and offer a verified-planning version.
- Do not auto-submit orders, pay, store credentials/cookies, bypass captchas, bypass queues, evade platform limits, or run high-frequency scraping.
- Stop before any paid or irreversible action. Ask for explicit user confirmation at review pages such as `提交订单`, `确认购买`, or `支付`.
- Treat price crawling as low-frequency evidence collection from official or authorized public sources, not as anti-bot automation.
- Do not build a booking engine, PDF renderer, HTML map, or visualization unless the user separately asks for it.

## Output Shape

Default to these sections unless the user requests another format:

1. 一句话结论
2. 推荐城市或路线
3. 每日行程表
4. 热门地点排序
5. 预算估算
6. 专项建议
7. 避坑清单
8. 备选版本
9. 出发前核验清单

For booking-lock requests, add:

10. 实时核验证据表
11. 锁定版本
12. 用户需亲自确认/支付的动作

## References

- `references/travel-guide-template.md`: guide structure, city tiers, child-age rules, summer risks, Xiaohongshu angle.
- `references/booking-lockin-workflow.md`: lock-state output, booking-readiness sequence, and user-confirmation boundaries.
- `references/price-verification-workflow.md`: live price/source verification, evidence tables, and comparison rules.
