#!/usr/bin/python
# -*- coding: UTF-8 -*-


zestaw_pusty = set()

trudniejsze_2009 = (
    set(range(3963, 4090 + 1))
    | set(range(4099, 4114 + 1))
    | set(range(4120, 4153 + 1))
    | set(range(4154, 4169 + 1))
    | set(range(1, 1 + 1))
    )

druga_lista = [1607, ]
faktury_usuniete_styczen_2010 = set([
    2553, 2581, 2722, 2865, 2947, 2977, 3063, 3083, 3207, 3274, 3448, 3503, 3534, 3535, 3799,
    2962, 3033, 3222, 3989, 3999, 4000, 4060, 4034, 3996, 4008, 3987, 3991, 4031, 3965
    ])
faktury_usuniete_kwiecien_2010 = set([
    4302, 4424, 4447, 4514, 4448, 4265, 4193]
    )

kwiecien_2010_i_wyjatek_g4 = (
    set(druga_lista)
    | set(range(4170, 4526 + 1))
    | set(range(6687, 6689 + 1))
    - faktury_usuniete_kwiecien_2010
    )

rdzen_2009 = (set(range(2467, 3930 + 1)) - faktury_usuniete_styczen_2010)
zestaw_t7 = (set(range(4559, 5284 + 1)))
zestaw_t8 = (set(range(5346, 5533 + 1)))
zestaw_t9 = (set(range(5838, 6114 + 1)))
zestaw_t10 = (set(range(6119, 6375 + 1)))
zestaw_t11 = (set(range(6376, 6686 + 1)))
zestaw_t13 = (set(range(6690, 7045 + 1)))
zestaw_t14 = (set(range(7046, 7296 + 1)))
zestaw_t15 = (set(range(7297, 7717 + 1)))
zestaw_t16 = (set(range(7721, 8256 + 1)))
zestaw_t17 = (set(range(8257, 8691 + 1)))
zestaw_t18 = (set(range(8692, 8815 + 1)))
zestaw_t21 = (set(range(8816, 9412 + 1)))
zestaw_t22 = (set(range(9413, 10093 + 1)))
zestaw_t23 = (set(range(10094, 10647 + 1)))
zestaw_t24 = (set(range(10648, 10765 + 1)))
zestaw_t25 = set(range(10766, 11187 + 1))
zestaw_t26 = set(range(11188, 11639 + 1))
zestaw_t27_t28 = set(range(11640, 12467 + 1))
zestaw_t29 = set(range(12468, 12632 + 1))
zestaw_t30_t31 = frozenset(range(12633, 13353 + 1))
zestaw_t32_t33 = frozenset(range(13354, 13736 + 1))
zestaw_t34_t35 = frozenset(range(13737, 14130 + 1))
zestaw_t36_t37 = frozenset(range(14131, 14721 + 1))
zestaw_t38 = frozenset(range(14722, 15199 + 1))
zestaw_t39 = frozenset(range(15200, 15376 + 1))
zestaw_t40 = frozenset(range(15377, 16861 + 1))


skasowane_nakladki_z_t7 = set([
    4564, 4565, 4566, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4576,
    4577, 4578, 4579, 4580, 4581, 4582, 4584, 4587, 4588, 4589, 4590, 4591,
    4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603,
    4604, 4605, 4606, 4607, 4608, 4609, 4610, 4611, 4612, 4613, 4614, 4615,
    4616, 4617, 4618, 4619, 4620, 4621, 4622, 4623, 4624, 4625, 4626, 4627,
    4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638, 4639,
    4640, 4641, 4642, 4643, 4644, 4645, 4646, 4647, 4648, 4649, 4650, 4651,
    4652, 4653, 4654, 4655, 4656, 4657, 4658, 4659, 4660, 4661, 4662, 4664,
    4665, 4666, 4667, 4668, 4669, 4670, 4671, 4672, 4673, 4674, 4675, 4676,
    4677, 4678, 4679, 4680, 4681, 4682, 4683, 4684, 4685, 4686, 4687, 4688,
    4689, 4690, 4691, 4692, 4693, 4694, 4696, 4697, 4698, 4699, 4700, 4701,
    4704, 4705, 4706, 4707, 4708, 4709, 4710, 4711, 4712, 4713, 4714, 4715,
    4716, 4717, 4718, 4719, 4720, 4721, 4722, 4723, 4724, 4725, 4726, 4727,
    4728, 4729, 4730, 4731, 4732, 4733, 4734, 4735, 4736, 4737, 4738, 4739,
    4740, 4741, 4742, 4743, 4744, 4745, 4746, 4747, 4748, 4749, 4750, 4751,
    4752, 4753, 4754, 4755, 4756, 4757, 4758, 4759, 4760, 4761, 4762, 4763,
    4764, 4765, 4766, 4768, 4769, 4770, 4771, 4772, 4773, 4774, 4775, 4776,
    4777, 4778, 4779, 4780, 4781, 4782, 4783, 4784, 4785, 4786, 4787, 4788,
    4789, 4790, 4791, 4792, 4793, 4794, 4795, 4796, 4797, 4798, 4799, 4800,
    4801, 4802, 4803, 4806, 4807, 4808, 4809, 4810, 4811, 4812, 4813, 4814,
    4816, 4817, 4818, 4819, 4820, 4821, 4822, 4823, 4824, 4825, 4826, 4827,
    4828, 4829, 4830, 4831, 4832, 4833, 4834, 4835, 4836, 4837, 4838, 4839,
    4840, 4841, 4842, 4843, 4844, 4845, 4846, 4847, 4848, 4849, 4850, 4851,
    4852, 4853, 4854, 4855, 4856, 4857, 4858, 4859, 4860, 4861, 4862, 4863,
    4864, 4865, 4866, 4867, 4868, 4869, 4870, 4871, 4872, 4873, 4874, 4875,
    4876, 4877, 4878, 4879, 4880, 4881, 4882, 4883, 4884, 4885, 4886, 4887,
    4888, 4889, 4890, 4891, 4892, 4893, 4894, 4895, 4896, 4897, 4898, 4899,
    4900, 4901, 4902, 4903, 4904, 4905, 4906, 4907, 4908, 4909, 4910, 4911,
    4912
    ])

dodatki_t6_sosw_sp35 = (
    set(range(5285, 5327 + 1))
    | set(range(5328, 5329 + 1))
    )

faza_kwiecien_2010 = (
    rdzen_2009
    | trudniejsze_2009
    | kwiecien_2010_i_wyjatek_g4
    )

faza_lipiec_2010 = (
    zestaw_t7
    - skasowane_nakladki_z_t7
    )

faza_wrzesien_2010 = (zestaw_t8)
odblokowane_sp2_filia = (set(range(5330, 5345 + 1)))
faza_kwiecien_2011 = (zestaw_t11)

fk_atmt_zolte = (
    zestaw_t39
    | zestaw_pusty
    )

fk_atmt_purpurowe = (
    zestaw_t22
    | faza_kwiecien_2010
    | faza_lipiec_2010
    | dodatki_t6_sosw_sp35
    | odblokowane_sp2_filia
    | faza_wrzesien_2010
    | set(range(6116, 6118 + 1))
    | zestaw_t9
    | zestaw_t10
    | zestaw_t11
    | zestaw_t13
    | zestaw_t14
    | zestaw_t15
    | zestaw_t16
    | zestaw_t17
    | zestaw_t18
    | zestaw_t21
    | zestaw_t23
    | zestaw_t24
    | zestaw_t25
    | zestaw_t26
    | zestaw_t27_t28
    | zestaw_t29
    | zestaw_t30_t31
    | zestaw_t32_t33
    | zestaw_t34_t35
    | zestaw_t38
    | zestaw_t36_t37
    | zestaw_pusty
    )

fk_atmt_turkusowe = (
    zestaw_t40
    | zestaw_pusty
    )

wszystkie_dotychczasowe_automatyczne = (
    fk_atmt_zolte
    | fk_atmt_turkusowe
    | fk_atmt_purpurowe
    )
